#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from arcane.util import ResStream
from .MobileInfo import MobileInfo


class MerchantInfo(MobileInfo):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.merchant_trade_type = stream.read_dword()
        self.merchant_std_buy_margin = stream.read_float()
        self.merchant_std_sell_margin = stream.read_float()
        self.merchant_guild_buy_margin = stream.read_float()
        self.merchant_guild_sell_margin = stream.read_float()
        self.merchant_nation_buy_margin = stream.read_float()
        self.merchant_nation_sell_margin = stream.read_float()
        num_buy_list = stream.read_dword()
        self.merchant_buy_list = [[
            stream.read_qword(),
            stream.read_dword(),
        ] for _ in range(num_buy_list)]
        num_sell_list = stream.read_dword()
        self.merchant_sell_list = [[
            stream.read_qword(),
            stream.read_dword(),
        ] for _ in range(num_sell_list)]

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_dword(self.merchant_trade_type)
        stream.write_float(self.merchant_std_buy_margin)
        stream.write_float(self.merchant_std_sell_margin)
        stream.write_float(self.merchant_guild_buy_margin)
        stream.write_float(self.merchant_guild_sell_margin)
        stream.write_float(self.merchant_nation_buy_margin)
        stream.write_float(self.merchant_nation_sell_margin)
        stream.write_dword(len(self.merchant_buy_list))
        for l in self.merchant_buy_list:
            stream.write_qword(l[0])
            stream.write_dword(l[1])
        stream.write_dword(len(self.merchant_sell_list))
        for l in self.merchant_sell_list:
            stream.write_qword(l[0])
            stream.write_dword(l[1])
