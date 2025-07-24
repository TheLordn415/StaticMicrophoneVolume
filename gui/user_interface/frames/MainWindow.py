# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 200))
        MainWindow.setMaximumSize(QSize(400, 200))
        icon = QIcon()
        icon.addFile(u":/images/images/microphone-black-shape.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.devicesList = QComboBox(self.centralwidget)
        self.devicesList.addItem("")
        self.devicesList.setObjectName(u"devicesList")
        self.devicesList.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.devicesList.sizePolicy().hasHeightForWidth())
        self.devicesList.setSizePolicy(sizePolicy1)
        self.devicesList.setMinimumSize(QSize(0, 22))
        self.devicesList.setMaximumSize(QSize(400, 22))
        self.devicesList.setEditable(False)

        self.verticalLayout.addWidget(self.devicesList)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 5, -1)
        self.volumeValue = QLineEdit(self.centralwidget)
        self.volumeValue.setObjectName(u"volumeValue")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.volumeValue.sizePolicy().hasHeightForWidth())
        self.volumeValue.setSizePolicy(sizePolicy2)
        self.volumeValue.setMinimumSize(QSize(100, 22))
        self.volumeValue.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_4.addWidget(self.volumeValue)

        self.lbVolume = QLabel(self.centralwidget)
        self.lbVolume.setObjectName(u"lbVolume")
        self.lbVolume.setMinimumSize(QSize(0, 22))
        self.lbVolume.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbVolume)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 0, 5, -1)
        self.intervalValue = QLineEdit(self.centralwidget)
        self.intervalValue.setObjectName(u"intervalValue")
        sizePolicy2.setHeightForWidth(self.intervalValue.sizePolicy().hasHeightForWidth())
        self.intervalValue.setSizePolicy(sizePolicy2)
        self.intervalValue.setMinimumSize(QSize(100, 22))
        self.intervalValue.setMaximumSize(QSize(16777215, 16777215))
        self.intervalValue.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.intervalValue)

        self.lbInterval = QLabel(self.centralwidget)
        self.lbInterval.setObjectName(u"lbInterval")
        sizePolicy1.setHeightForWidth(self.lbInterval.sizePolicy().hasHeightForWidth())
        self.lbInterval.setSizePolicy(sizePolicy1)
        self.lbInterval.setMinimumSize(QSize(0, 22))
        self.lbInterval.setMaximumSize(QSize(16777215, 16777215))
        self.lbInterval.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbInterval)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.pbrun = QPushButton(self.centralwidget)
        self.pbrun.setObjectName(u"pbrun")
        self.pbrun.setMinimumSize(QSize(75, 45))
        self.pbrun.setMaximumSize(QSize(110, 45))

        self.horizontalLayout.addWidget(self.pbrun)

        self.pbminimize = QPushButton(self.centralwidget)
        self.pbminimize.setObjectName(u"pbminimize")
        self.pbminimize.setMinimumSize(QSize(75, 45))
        self.pbminimize.setMaximumSize(QSize(110, 45))

        self.horizontalLayout.addWidget(self.pbminimize)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pbminimize.clicked.connect(MainWindow.showMinimized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Static Microphone Volume", None))
        self.devicesList.setItemText(0, QCoreApplication.translate("MainWindow", u"...", None))

        self.volumeValue.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type volume from 0% to 100%", None))
        self.lbVolume.setText(QCoreApplication.translate("MainWindow", u"Volume", None))
        self.intervalValue.setText("")
        self.intervalValue.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type interval in seconds", None))
        self.lbInterval.setText(QCoreApplication.translate("MainWindow", u"Interval", None))
        self.pbrun.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pbminimize.setText(QCoreApplication.translate("MainWindow", u"Minimize", None))
    # retranslateUi

