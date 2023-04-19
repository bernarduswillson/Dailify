from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import os

from MasterManager import *
from UserManager import *

class LoadingPage(QWidget):
    def __init__(self, parent=None):
        super(LoadingPage, self).__init__(parent)
        loadUi('src/uibuilder/LoadingPage.ui', self)
        fontMB = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Bold.otf"))
        fontMM = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Medium.otf"))
        self.fontFamilyMB = QFontDatabase.applicationFontFamilies(fontMB)[0]
        self.fontFamilyMM = QFontDatabase.applicationFontFamilies(fontMM)[0]

        fontHeader = QFont(self.fontFamilyMB, 48, 75)
        fontLoadingMsg = QFont(self.fontFamilyMM, 18)
        fontVersion = QFont(self.fontFamilyMM, 12)

        self.Header.setFont(fontHeader)
        self.LoadingMsg.setFont(fontLoadingMsg)
        self.Version.setFont(fontVersion)

    def intro(self):
        self.Header.setText("Dailify.")
        self.Header.setStyleSheet("color: rgba(143,115,101,0);")
        self.LoadingMsg.setText("")

        for i in range(1, 1002):
            alpha = i / 1000.0  # Calculate alpha as a float value between 0.001 and 1
            QTimer.singleShot(int(i), lambda a=alpha: self.Header.setStyleSheet("color: rgba(143, 115, 101, {});".format(a)))

        for i in range(1, 1002):
            alpha = i / 1000.0
            QTimer.singleShot(int(2000 + i), lambda a=alpha: self.Header.setStyleSheet("color: rgba(143, 115, 101, {});".format(1-a)))

    def loading(self):
        if not MasterManager.checkDB():
            MasterManager.createSetupDB()
            
        self.LoadingMsg.setText("Getting things ready")

        if MasterManager.checkDB():
            self.Header.setText("Welcome, " + UserManager.getUser()[1])
        
        for i in range(1, 1002):
            alpha = i / 1000.0
            QTimer.singleShot(int(i), lambda a=alpha: self.LoadingMsg.setStyleSheet("color: rgba(220, 220, 220, {});".format(a)))
        for i in range(1, 1002):
            alpha = i / 1000.0
            QTimer.singleShot(int(i), lambda a=alpha: self.Header.setStyleSheet("color: rgba(143, 115, 101, {});".format(a)))
        
        QTimer.singleShot(500, lambda: self.LoadingMsg.setText("Getting things ready ."))
        QTimer.singleShot(1000, lambda: self.LoadingMsg.setText("Getting things ready . ."))
        QTimer.singleShot(1500, lambda: self.LoadingMsg.setText("Getting things ready . . ."))
        QTimer.singleShot(2000, lambda: self.LoadingMsg.setText("Getting things ready"))
        QTimer.singleShot(2500, lambda: self.LoadingMsg.setText("Getting things ready ."))
        QTimer.singleShot(3000, lambda: self.LoadingMsg.setText("Getting things ready . ."))

        for i in range(1, 1002):
            alpha = i / 1000.0
            QTimer.singleShot(int(3000 + i), lambda a=alpha: self.Header.setStyleSheet("color: rgba(143, 115, 101, {});".format(1-a)))
        for i in range(1, 1002):
            alpha = i / 1000.0
            QTimer.singleShot(int(3000 + i), lambda a=alpha: self.LoadingMsg.setStyleSheet("color: rgba(220, 220, 220, {});".format(1-a)))

        