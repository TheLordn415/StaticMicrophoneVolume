from typing import List

from PySide6.QtWidgets import QApplication

from gui.user_interface.main_window import MainWindow
from resources import qt_resource_container_rc


class UIApplication(QApplication):
    def __init__(self, argv: List[str]):
        super(UIApplication, self).__init__(argv)

        self.main_window = MainWindow()
        self.main_window.show()