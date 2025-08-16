import sys
import multiprocessing

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


if __name__ == "__main__":
    main()
