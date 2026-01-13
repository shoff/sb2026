#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from arcane.util import ResStream
from .MobileInfo import MobileInfo


class ShopKeeperInfo(MobileInfo):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.shopkeeper_shop_type = stream.read_dword()
        self.shopkeeper_start_gold = stream.read_dword()
        self.shopkeeper_std_buy_percent = stream.read_float()
        self.shopkeeper_std_sell_percent = stream.read_float()
        self.shopkeeper_nation_buy_percent = stream.read_float()
        self.shopkeeper_nation_sell_percent = stream.read_float()
        num_buy_list = stream.read_dword()
        self.shopkeeper_buy_list = [[
            stream.read_qword(),
            stream.read_dword(),
        ] for _ in range(num_buy_list)]
        num_sell_list = stream.read_dword()
        self.shopkeeper_sell_list = [[
            stream.read_qword(),
            stream.read_dword(),
        ] for _ in range(num_sell_list)]

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_dword(self.shopkeeper_shop_type)
        stream.write_dword(self.shopkeeper_start_gold)
        stream.write_float(self.shopkeeper_std_buy_percent)
        stream.write_float(self.shopkeeper_std_sell_percent)
        stream.write_float(self.shopkeeper_nation_buy_percent)
        stream.write_float(self.shopkeeper_nation_sell_percent)
        stream.write_dword(len(self.shopkeeper_buy_list))
        for l in self.shopkeeper_buy_list:
            stream.write_qword(l[0])
            stream.write_dword(l[1])
        stream.write_dword(len(self.shopkeeper_sell_list))
        for l in self.shopkeeper_sell_list:
            stream.write_qword(l[0])
            stream.write_dword(l[1])
