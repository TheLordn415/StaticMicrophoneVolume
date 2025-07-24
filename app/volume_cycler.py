import time
from controllers.volume_controller import MicrophoneVolumeController


class VolumeCycler:
    """Runs an infinite loop to set the volume repeatedly"""

    def __init__(self, controller: MicrophoneVolumeController, volume: int, interval: float):
        self.controller = controller
        self.volume = volume
        self.interval = interval

    def start(self):
        print(f"\nCycling volume to {self.volume}% every {self.interval} seconds...")
        try:
            while True:
                self.controller.set_volume(self.volume)
                print(f"Volume set to {self.volume}%")
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("\nStopped by user.")
