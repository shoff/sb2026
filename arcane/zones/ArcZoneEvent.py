#  • ▌ ▄ ·. ▄▄▄▄·     ▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄       ▄▄▄·▄▄▄       
#  ·██ ▐███▪▐█ ▀█▪    ▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·    ▐█ ▄█▀▄ █·▪    
#  ▐█ ▌▐▌▐█·▐█▀▀█▄    ▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄      ██▀·▐▀▀▄  ▄█▀▄
#  ██ ██▌▐█▌██▄▪▐█    ▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▪·•▐█•█▌▐█▌.▐▌
#  ▀▀  █▪▀▀▀·▀▀▀▀      ▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀    .▀   .▀  ▀ ▀█▄▀▪
#                Magicbane Emulator Project © 2013 - 2022
#                           www.magicbane.com

from arcane.util import ResStream


class ArcZTriggerAction:
    def load_binary(self, stream: ResStream):
        self.zone_trigger_action_type = stream.read_dword()
        self.zone_trigger_action_unknown1 = stream.read_bool()
        self.zone_trigger_action_is_timed = stream.read_bool()
        self.zone_trigger_action_unknown2 = stream.read_bool()

        if self.zone_trigger_action_is_timed:
            self.zone_trigger_action_time_begin = stream.read_float()
            self.zone_trigger_action_time_end = stream.read_float()
        self.zone_trigger_action_has_state = stream.read_bool()
        if self.zone_trigger_action_has_state:
            self.zone_trigger_action_new_state = stream.read_dword()
        num_specifics = stream.read_dword()
        self.zone_trigger_action_specifics = [stream.read_dword() for _ in range(num_specifics)]
        num_items = stream.read_dword()
        self.zone_trigger_action_items = [stream.read_dword() for _ in range(num_items)]
        num_parent_states = stream.read_dword()
        self.zone_trigger_action_parent_states = [stream.read_dword() for _ in range(num_parent_states)]


class ArcZoneEventInfo:
    def load_binary(self, stream: ResStream):
        self.zone_event_recycle = stream.read_dword()
        self.zone_event_spawn_radius = stream.read_float()
        self.zone_event_fc_label = stream.read_string()
        self.zone_event_event_name = stream.read_string()
        self.zone_event_unknown1 = stream.read_dword()
        self.zone_event_spawn_location = stream.read_tuple()
        self.zone_event_parent_name = stream.read_string()
        self.zone_event_unknown2 = stream.read_dword()
        self.zone_event_unknown3 = stream.read_bool()
        num_triggers = stream.read_dword()
        self.zone_event_triggers = [ArcZTriggerAction() for _ in range(num_triggers)]
        for action in self.zone_event_triggers:
            action.load_binary(stream)


class ArcZoneEvent:
    def load_binary(self, stream: ResStream):
        self.zone_event_type = stream.read_dword()

        if self.zone_event_type == 1:
            self.zone_event_data = ArcZoneEventInfo()
            self.zone_event_data.load_binary(stream)
        elif self.zone_event_type == 2:
            self.zone_event_data = ArcZoneEventInfo()
            self.zone_event_data.load_binary(stream)
        elif self.zone_event_type == 3:
            self.zone_event_data = ArcZoneEventInfo()
            self.zone_event_data.load_binary(stream)
