import warnings
from typing import Optional
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

from pycaw.utils import AudioDevice

warnings.filterwarnings("ignore", category=UserWarning, module="pycaw.utils")

class MicrophoneVolumeController:
    """Controls microphone volume on Windows via pycaw"""

    def __init__(self, device_name: str):
        self.device_name = device_name
        self.volume_interface = self._get_volume_interface()

    def _get_volume_interface(self) -> Optional[IAudioEndpointVolume]:
        """Finds the volume control interface for the given device"""
        devices = AudioUtilities.GetAllDevices()
        for dev in devices:
            if not isinstance(dev, AudioDevice):
                continue
            if dev.FriendlyName and dev.FriendlyName.startswith(self.device_name):
                interface = dev._dev.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
                )
                return cast(interface, POINTER(IAudioEndpointVolume))
        return None

    def set_volume(self, level_percent: int):
        """Sets the microphone volume to a given percentage"""
        if self.volume_interface:
            level = max(0.0, min(level_percent / 100.0, 1.0))
            self.volume_interface.SetMasterVolumeLevelScalar(level, None)
        else:
            raise RuntimeError("Volume interface not found for device")
