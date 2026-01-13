
from collections import OrderedDict
from arcane.util import ResStream

MAGIC_SKEL = b'SKEL'
CURRENT_VERSION = 3


class ArcBoneRecord(object):
    __slots__ = ('name_hash', 'parent_index', 'flags', 'bind_pose_matrix', 'name')

    def __init__(self):
        self.name_hash = 0
        self.parent_index = -1  # -1 denotes root
        self.flags = 0          # attachment / billboard bits
        self.bind_pose_matrix = [0.0] * 16
        self.name = None        # optional string name when available

    # ────────────────────────── binary ──────────────────────────

    def load_binary(self, stream: ResStream):
        self.name_hash = stream.read_dword()

        raw_parent = stream.read_word()
        # Treat as signed int16
        if raw_parent >= 0x8000:
            raw_parent -= 0x10000
        self.parent_index = raw_parent

        self.flags = stream.read_word()
        self.bind_pose_matrix = [stream.read_float() for _ in range(16)]

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.name_hash)
        stream.write_word(self.parent_index & 0xFFFF)
        stream.write_word(self.flags)
        for value in self.bind_pose_matrix:
            stream.write_float(value)

    # ────────────────────────── json ──────────────────────────

    def load_json(self, data):
        self.name_hash = data['name_hash']
        self.parent_index = data['parent_index']
        self.flags = data['flags']
        self.bind_pose_matrix = data['bind_pose_matrix']
        self.name = data.get('name')

    def save_json(self):
        out = OrderedDict([
            ('name_hash', self.name_hash),
            ('parent_index', self.parent_index),
            ('flags', self.flags),
            ('bind_pose_matrix', self.bind_pose_matrix),
        ])
        if self.name is not None:
            out['name'] = self.name
        return out


class ArcSkeleton(object):
    """In-memory representation of Shadowbane *.skel* files (see asset-loading.md)."""

    def __init__(self):
        self.version = CURRENT_VERSION
        self.flags = 0
        self.bones = []          # type: list[ArcBoneRecord]
        self.motion_tokens = []  # type: list[int]

    # ────────────────────────── binary ──────────────────────────

    def load_binary(self, stream: ResStream):
        # Support two observed formats:
        # 1) 'SKEL' magic, then version/counts/flags
        # 2) UTF-16 length-prefixed string (e.g., 'skeleton'), then animations table, then bones
        pos = stream.buffer.tell()
        head = stream.read_bytes(4)
        if head == MAGIC_SKEL:
            # Original format
            self.version = stream.read_dword()
            bone_count = stream.read_word()
            motion_count = stream.read_word()
            self.flags = stream.read_dword()

            self.bones = []
            for _ in range(bone_count):
                bone = ArcBoneRecord()
                bone.load_binary(stream)
                self.bones.append(bone)

            self.motion_tokens = [stream.read_dword() for _ in range(motion_count)]
            return

        # Alternate format: rewind and parse string name, then animations, then bones
        stream.buffer.seek(pos)
        _name = stream.read_string()  # e.g., 'skeleton'

        # Animations list (ids referencing Motion.cache)
        try:
            anim_count = stream.read_dword()
        except Exception:
            anim_count = 0
        motion_tokens: list[int] = []
        for _ in range(anim_count):
            # Layout per C++: 4 bytes skip, 4 bytes id, 8 bytes skip
            try:
                _skip_a = stream.read_dword()
                anim_id = stream.read_dword()
                if anim_id > 0:
                    motion_tokens.append(anim_id)
                # skip two dwords
                _skip_b = stream.read_dword()
                _skip_c = stream.read_dword()
            except Exception:
                break

        # Bones: read until we can no longer parse a full record
        bones: list[ArcBoneRecord] = []
        nchildren: list[int] = []
        while True:
            try:
                # Probe if at EOF: attempt to read next dword of id
                peek_pos = stream.buffer.tell()
                maybe_id = stream.read_bytes(4)
                if len(maybe_id) < 4:
                    break
                stream.buffer.seek(peek_pos)

                # Bone id (use as name_hash surrogate)
                bone_id = stream.read_dword()

                # UTF-16 bone name
                bone_name = stream.read_string()

                # Direction (Vec3)
                _dir_x, _dir_y, _dir_z = stream.read_tuple()
                # Length
                _length = stream.read_float()
                # Axis (Vec3)
                _axis_x, _axis_y, _axis_z = stream.read_tuple()

                # Skip flags string
                try:
                    flen = stream.read_dword()
                    if flen > 0:
                        _ = stream.read_bytes(flen * 2)
                except Exception:
                    flen = 0

                # Skip 36 bytes of unused data
                _ = stream.read_bytes(36)

                # Flip flag and unknown flag
                _flip = stream.read_byte()
                _unknown = stream.read_byte()

                # Number of children
                child_count = stream.read_dword()

                b = ArcBoneRecord()
                b.name_hash = bone_id
                b.parent_index = -1
                b.flags = 0
                b.name = bone_name
                # No bind-pose provided in this format; use identity
                b.bind_pose_matrix = [1.0, 0.0, 0.0, 0.0,
                                      0.0, 1.0, 0.0, 0.0,
                                      0.0, 0.0, 1.0, 0.0,
                                      0.0, 0.0, 0.0, 1.0]
                bones.append(b)
                nchildren.append(child_count)
            except Exception:
                break

        # Reconstruct parent indices based on sequential layout and nChildren
        setup = [False] * len(bones)
        next_idx = 1

        def assign(idx: int, parent: int):  # noqa: ANN001
            nonlocal next_idx
            bones[idx].parent_index = parent
            setup[idx] = True
            for _ in range(nchildren[idx] if idx < len(nchildren) else 0):
                # find next unused bone
                while next_idx < len(bones) and setup[next_idx]:
                    next_idx += 1
                if next_idx >= len(bones):
                    return
                child = next_idx
                next_idx += 1
                assign(child, idx)

        if bones:
            assign(0, -1)

        self.version = CURRENT_VERSION
        self.flags = 0
        self.bones = bones
        self.motion_tokens = motion_tokens
        return

    # ────────────────────────── json ──────────────────────────

    def load_json(self, data):
        self.version = data.get('version', CURRENT_VERSION)
        self.flags = data.get('flags', 0)

        self.bones = []
        for bone_data in data.get('bones', []):
            bone = ArcBoneRecord()
            bone.load_json(bone_data)
            self.bones.append(bone)

        self.motion_tokens = data.get('motion_tokens', [])

    def save_json(self):
        return OrderedDict([
            ('version', self.version),
            ('flags', self.flags),
            ('bones', [b.save_json() for b in self.bones]),
            ('motion_tokens', self.motion_tokens),
        ])
