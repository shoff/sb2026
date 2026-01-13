from collections import OrderedDict

from arcane.enums.zone.arc_mobile import *
from arcane.util import ResStream
from .mobile.HirelingInfo import HirelingInfo
from .mobile.MerchantInfo import MerchantInfo
from .mobile.MinionInfo import MinionInfo
from .mobile.MobileInfo import MobileInfo
from .mobile.ShopKeeperInfo import ShopKeeperInfo
from .mobile.TrainerInfo import TrainerInfo


class ArcMobile:

    def load_binary(self, stream: ResStream):
        self.mobile_type = stream.read_dword()

        if self.mobile_type == 1:
            self.mobile_data = MobileInfo()
            self.mobile_data.load_binary(stream)
        elif self.mobile_type == 2:
            self.mobile_data = MobileInfo()
            self.mobile_data.load_binary(stream)
        elif self.mobile_type == 3:
            self.mobile_data = ShopKeeperInfo()
            self.mobile_data.load_binary(stream)
        elif self.mobile_type == 4:
            self.mobile_data = TrainerInfo()
            self.mobile_data.load_binary(stream)
        elif self.mobile_type == 8:
            self.mobile_data = MerchantInfo()
            self.mobile_data.load_binary(stream)
        elif self.mobile_type == 9:
            self.mobile_data = HirelingInfo()
            self.mobile_data.load_binary(stream)
        elif self.mobile_type == 10:
            self.mobile_data = HirelingInfo()
            self.mobile_data.load_binary(stream)
        elif self.mobile_type == 11:
            self.mobile_data = MinionInfo()
            self.mobile_data.load_binary(stream)

    def save_binary(self, stream: ResStream):
        stream.write_dword(self.mobile_type)
        self.mobile_data.save_binary(stream)

    def save_json(self):
        data = OrderedDict()
        data['mobile_type'] = MOBILE_TO_STRING[self.mobile_type]
        data['mobile_data'] = self.mobile_data.save_json()
        return data

    def load_json(self, data):
        self.mobile_type = STRING_TO_MOBILE[data['mobile_type']]
        if self.mobile_type == 1:
            self.mobile_data = MobileInfo()
        elif self.mobile_type == 2:
            self.mobile_data = MobileInfo()
        elif self.mobile_type == 3:
            self.mobile_data = ShopKeeperInfo()
        elif self.mobile_type == 4:
            self.mobile_data = TrainerInfo()
        elif self.mobile_type == 8:
            self.mobile_data = MerchantInfo()
        elif self.mobile_type == 9:
            self.mobile_data = HirelingInfo()
        elif self.mobile_type == 10:
            self.mobile_data = HirelingInfo()
        elif self.mobile_type == 11:
            self.mobile_data = MinionInfo()
        self.mobile_data.load_json(data['mobile_data'])
