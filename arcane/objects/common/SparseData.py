
from collections import OrderedDict

from arcane.enums.arc_sparse import *
from arcane.util import ResStream


class SparseData:
    def __init__(self) -> None:
        self.sp_data = OrderedDict()

    def load_binary(self, stream: ResStream):
        sparse_tag = stream.read_dword()
        while sparse_tag:
            sparse_type = SPARSE_TAG_TO_SPARSE_TYPE[sparse_tag]
            value = None

            if sparse_type == SPARSE_VAL_LONG:
                value = stream.read_dword()

            elif sparse_type == SPARSE_VAL_FLOAT:
                value = stream.read_float()

            elif sparse_type == SPARSE_VAL_BOOL:
                value = stream.read_bool()

            elif sparse_type == SPARSE_UID:
                value = stream.read_dword()

            elif sparse_type == SPARSE_REF_VECTOR3:
                value = stream.read_tuple()

            elif sparse_type == SPARSE_REF_ARC_STRING:
                value = stream.read_string()

            elif sparse_type == SPARSE_REF_MERCHANT_DATA:
                value = [
                    stream.read_qword(),
                    stream.read_qword(),
                    stream.read_dword(),
                ]

            elif sparse_type == SPARSE_REF_ARC_CACHE_ID:
                value = stream.read_qword()

            elif sparse_type == SPARSE_PTR_ACTION_RESPONSE:
                value = stream.read_dword()

            elif sparse_type == SPARSE_ENUM_ITEM_TYPE:
                value = stream.read_dword()

            self.sp_data[sparse_tag] = value
            sparse_tag = stream.read_dword()

    def save_binary(self, stream: ResStream):
        for tag, value in self.sp_data.items():
            stream.write_dword(tag)

            sparse_type = SPARSE_TAG_TO_SPARSE_TYPE[tag]
            if sparse_type == SPARSE_VAL_LONG:
                stream.write_dword(value)

            elif sparse_type == SPARSE_VAL_FLOAT:
                stream.write_float(value)

            elif sparse_type == SPARSE_VAL_BOOL:
                stream.write_bool(value)

            elif sparse_type == SPARSE_UID:
                stream.write_dword(value)

            elif sparse_type == SPARSE_REF_VECTOR3:
                stream.write_tuple(value)

            elif sparse_type == SPARSE_REF_ARC_STRING:
                stream.write_string(value)

            elif sparse_type == SPARSE_REF_MERCHANT_DATA:
                stream.write_qword(value[0])
                stream.write_qword(value[1])
                stream.write_qword(value[2])

            elif sparse_type == SPARSE_REF_ARC_CACHE_ID:
                stream.write_qword(value)

            elif sparse_type == SPARSE_PTR_ACTION_RESPONSE:
                stream.write_dword(value)

            elif sparse_type == SPARSE_ENUM_ITEM_TYPE:
                stream.write_dword(value)
        stream.write_dword(0)

    def load_json(self, data):
        for key, value in data.items():
            self.sp_data[STRING_TO_SPARSE_TAG[key]] = value

    def save_json(self):
        data = OrderedDict()
        for tag, value in self.sp_data.items():
            data[SPARSE_TAG_TO_STRING[tag]] = value
        return data
