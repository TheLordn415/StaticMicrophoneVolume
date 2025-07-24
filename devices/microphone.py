import pyaudio
from typing import List


class Microphone:
    """Represents an input audio device (microphone)"""

    def __init__(self, name: str, index: int):
        self.name = name
        self.index = index

    def __str__(self):
        return f"{self.index}: {self.name}"


class MicrophoneManager:
    """Manages the list of available microphones"""

    def __init__(self):
        self._pyaudio = pyaudio.PyAudio()

    def list_microphones(self) -> List[Microphone]:
        """Lists all input devices that can act as microphones"""
        microphones = []
        for i in range(self._pyaudio.get_device_count()):
            info = self._pyaudio.get_device_info_by_index(i)
            if info.get("maxInputChannels", 0) != 0 and info.get('hostApi', 0) == 0:
                microphones.append(Microphone(info.get("name", "Unknown"), i))
        return microphones
