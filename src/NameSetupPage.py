from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import os

from UserManager import *
from SetupModule import *
from Entity.User import *

class NameSetupPage(QWidget):
    def __init__(self, parent=None):
        super(NameSetupPage, self).__init__(parent)
        loadUi('src/uibuilder/ProfileSetup.ui', self)

        fontMB = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Bold.otf"))
        fontMM = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Medium.otf"))
        self.fontFamilyMB = QFontDatabase.applicationFontFamilies(fontMB)[0]
        self.fontFamilyMM = QFontDatabase.applicationFontFamilies(fontMM)[0]

        fontInputLabel = QFont(self.fontFamilyMB, 24, 75)
        fontNameInput = QFont(self.fontFamilyMM, 15)

        self.inputLabel.setFont(fontInputLabel)
        self.nameInput.setFont(fontNameInput)

        for i in range(1, 1002):
            alpha = i / 1000.0  # Calculate alpha as a float value between 0.001 and 1
            QTimer.singleShot(int(7000 + i), lambda a=alpha: self.inputLabel.setStyleSheet("color: rgba(143, 115, 101, {});".format(a)))
        for i in range(1, 1002):
            alpha = i / 1000.0  # Calculate alpha as a float value between 0.001 and 1
            QTimer.singleShot(int(7000 + i), lambda a=alpha: self.nameInput.setStyleSheet("background-color: rgba(40, 40, 40, {}); border-radius: 25px; color: rgba(129, 129, 129, {}); padding-left: 30px; margin-left: 500px; margin-right: 500px;".format(a, a)))

        QTimer.singleShot(8002, lambda: self.nameInput.setFocus())