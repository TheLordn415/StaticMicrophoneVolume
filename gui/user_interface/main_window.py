import multiprocessing
from ctypes import c_bool
from typing import Optional

from PySide6.QtCore import QEvent, QTimer
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu, QApplication

from controllers import MicrophoneVolumeController
from devices import MicrophoneManager
from gui.user_interface.frames.MainWindow import Ui_MainWindow
from workers import WorkerProcess


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self._setup_tray_icon()
        self.setFixedSize(self.size())

        self.manager: Optional[MicrophoneManager] = MicrophoneManager()
        self.controller: Optional[MicrophoneVolumeController] = None
        self.workerprocess: Optional[WorkerProcess] = None
        self.executable: Optional[multiprocessing.Value] = multiprocessing.Value(c_bool, False)

        self._check_worker_stopped_timer = QTimer()

        self._connect_signals()

        self._initDevicesList()

    def _connect_signals(self):
        self.pbminimize.clicked.connect(lambda: self._minimize_to_tray())
        self.pbrun.clicked.connect(self.start_button_clicked)
        self.devicesList.currentIndexChanged.connect(lambda: print(f"Selected device {self.devicesList.currentIndex()}: "
                                                                   f"{self.devicesList.itemText(self.devicesList.currentIndex())}"))
        self._check_worker_stopped_timer.timeout.connect(self._check_worker_stopped)

    def start_button_clicked(self):
        with self.executable.get_lock():
            if not self.executable.value:
                self.pbrun.setText("Running...")
                device_name = self.devicesList.itemText(self.devicesList.currentIndex())
                self.executable.value = True
                self.workerprocess = WorkerProcess(device_name=device_name, volume=int(self.volumeValue.text()),
                                                   interval=int(self.intervalValue.text()), executable=self.executable)
                self.workerprocess.start()
            elif self.executable.value:
                self.executable.value = False
                self._check_worker_stopped_timer.start(100)

    def _check_worker_stopped(self):
        if self.workerprocess and not self.workerprocess.is_alive():
            self._check_worker_stopped_timer.stop()
            self.workerprocess.join()
            self.pbrun.setText("Start")
            print(f"{self.workerprocess.name} has stopped")

    def _initDevicesList(self):
        self.devicesList.removeItem(0)
        microphones = self.manager.list_microphones()

        for device in microphones:
            self.devicesList.addItem(device.name)
            print(f"Device {device} added to list")

        self.devicesList.setEnabled(True)

    def _setup_tray_icon(self):
        """Setup system tray icon and menu"""
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(u":/images/images/microphone-black-shape.ico"))

        tray_menu = QMenu()

        restore_action = QAction("Restore", self)
        restore_action.triggered.connect(self._restore_from_tray)
        tray_menu.addAction(restore_action)

        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)

        self.tray_icon.activated.connect(self._on_tray_icon_activated)

    def _minimize_to_tray(self):
        """Minimize window and hide to system tray"""
        self.showMinimized()
        self.hide()
        self.tray_icon.show()

    def _restore_from_tray(self):
        """Restore window from system tray"""
        self.show()
        self.showNormal()
        self.raise_()
        self.activateWindow()
        self.tray_icon.hide()

    def _on_tray_icon_activated(self, reason):
        """Handle tray icon click"""
        if reason == QSystemTrayIcon.Trigger:
            if self.isHidden():
                self._restore_from_tray()
            else:
                self._minimize_to_tray()

    def changeEvent(self, event: QEvent):
        """Handle window state changes like minimize"""

        if event.type() == QEvent.Type.WindowStateChange:
            if self.isMinimized():
                self.hide()
                self.tray_icon.show()

                self.tray_icon.showMessage(
                    "Static Microphone Volume is minimized.",
                    "It is now running in the background. Click the icon to restore it.",
                    QSystemTrayIcon.Information,
                    5000
                )

        super().changeEvent(event)

    def closeEvent(self, event):
        """Handle window close event"""
        self.hide()

        self.executable.value = False
        self._check_worker_stopped()

        event.accept()
