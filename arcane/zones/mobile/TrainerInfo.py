#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from arcane.util import ResStream
from .MobileInfo import MobileInfo


class TrainerInfo(MobileInfo):
    def load_binary(self, stream: ResStream):
        super().load_binary(stream)
        self.trainer_std_profit_margin = stream.read_float()
        self.trainer_profit_margin = stream.read_float()

    def save_binary(self, stream: ResStream):
        super().save_binary(stream)
        stream.write_float(self.trainer_std_profit_margin)
        stream.write_float(self.trainer_profit_margin)

    def save_json(self):
        data = super().save_json()
        data['trainer_std_profit_margin'] = self.trainer_std_profit_margin
        data['trainer_profit_margin'] = self.trainer_profit_margin
        return data

    def load_json(self, data):
        super().load_json(data)
        self.trainer_std_profit_margin = data['trainer_std_profit_margin']
        self.trainer_profit_margin = data['trainer_profit_margin']
