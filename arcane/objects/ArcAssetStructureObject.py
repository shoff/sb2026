
from arcane.util import ResStream
from .ArcStructureObject import ArcStructureObject


class ArcAssetStructureObject(ArcStructureObject):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.asset_structure_template_id = stream.read_qword()

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_qword(self.asset_structure_template_id)

    def load_json(self, data):
        super().load_json(data)
        self.asset_structure_template_id = data['asset_structure_template_id']

    def save_json(self):
        data = super().save_json()
        data['asset_structure_template_id'] = self.asset_structure_template_id
        return data
