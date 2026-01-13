from wave import Wave_read, Wave_write

from arcane.util import ResStream


class ArcSound:
    def load_binary(self, stream: ResStream):
        data_size = stream.read_dword()
        self.sound_frame_rate = stream.read_dword()
        self.sound_n_channels = stream.read_dword()
        self.sound_sample_width = stream.read_dword()
        self.sound_data = stream.read_bytes(data_size)

    def save_binary(self, stream: ResStream):
        data_size = len(self.sound_data)
        stream.write_dword(data_size)
        stream.write_dword(self.sound_frame_rate)
        stream.write_dword(self.sound_n_channels)
        stream.write_dword(self.sound_sample_width)
        stream.write_bytes(self.sound_data)

    def load_wav(self, stream: Wave_read):
        self.sound_frame_rate = stream.getframerate()
        self.sound_n_channels = stream.getnchannels()
        self.sound_sample_width = stream.getsampwidth() * 8
        self.sound_data = stream.readframes(stream.getnframes())

    def save_wav(self, stream: Wave_write):
        stream.setframerate(self.sound_frame_rate)
        stream.setnchannels(self.sound_n_channels)
        stream.setsampwidth(self.sound_sample_width // 8)
        stream.writeframes(self.sound_data)
