import multiprocessing
import time

from controllers import MicrophoneVolumeController


class WorkerProcess(multiprocessing.Process):
    def __init__(self, device_name: str, volume: int, interval: int, executable: multiprocessing.Value):
        super().__init__(daemon=True, name="WorkerSetVolume")
        self.device_name = device_name
        self.controller = None
        self.volume = volume
        self.interval = interval
        self.executable = executable

    def run(self):
        self.controller = MicrophoneVolumeController(device_name=self.device_name)
        while self.executable.value:
            self.controller.set_volume(self.volume)
            print(f"Volume set to {self.volume}%")
            for _ in range(self.interval):
                if not self.executable.value:
                    break
                time.sleep(1)

        else:
            self.close()
