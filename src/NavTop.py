from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import os

class NavTop(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi("src/uibuilder/NavTop.ui", self)

        # Font
        fontMB = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Bold.otf"))
        fontMM = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Medium.otf"))
        self.fontFamilyMB = QFontDatabase.applicationFontFamilies(fontMB)[0]
        self.fontFamilyMM = QFontDatabase.applicationFontFamilies(fontMM)[0]

        self.DashboardLabel.setFont(QFont(self.fontFamilyMM, 15))
        self.DailifyLabel.setFont(QFont(self.fontFamilyMB, 15, 75))