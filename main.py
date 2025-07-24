import sys
import multiprocessing

from devices import MicrophoneManager
from controllers import MicrophoneVolumeController
from app import VolumeCycler
from gui.user_interface.application import UIApplication


def main():
    multiprocessing.freeze_support()
    multiprocessing.set_start_method("spawn")

    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        print("Application crashed!", exctype, value, traceback)
        sys._excepthook(exctype, value, traceback)

    sys.excepthook = exception_hook

    app = UIApplication(sys.argv)
    app.setApplicationName("StaticMicrophoneVolume")

    sys.exit(app.exec())


def previous_main():
    manager = MicrophoneManager()
    microphones = manager.list_microphones()

    if not microphones:
        print("No microphones found.")
        return

    print("Available microphones:")
    for mic in microphones:
        print(mic)

    index = int(input("\nEnter the index of the microphone to control: "))
    selected_mic = next((m for m in microphones if m.index == index), None)

    if not selected_mic:
        print("Invalid microphone index.")
        return

    volume = int(input("Enter the target volume (0-100): "))
    interval = float(input("Enter the interval in seconds: "))

    controller = MicrophoneVolumeController(selected_mic.name)
    cycler = VolumeCycler(controller, volume, interval)
    cycler.start()


if __name__ == "__main__":
    main()
