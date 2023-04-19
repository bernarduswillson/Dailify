from PyQt5.QtWidgets import * 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
import os

from MasterManager import *

from SetupModule import *
from ProgramModule import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('src/uibuilder/Window.ui', self)

        icon=QIcon("src/assets/icon.jpg")
        self.setWindowIcon(icon)

        # Initialize Font
        fontMB = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Bold.otf"))
        fontMM = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Medium.otf"))
        fontMR = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Regular.otf"))

        # Initialize Family
        self.fontFamilyMB = QFontDatabase.applicationFontFamilies(fontMB)[0]
        self.fontFamilyMM = QFontDatabase.applicationFontFamilies(fontMM)[0]
        self.fontFamilyMR = QFontDatabase.applicationFontFamilies(fontMR)[0]

        # Initialize Pages
        self.CentralStack = QStackedWidget(self)
        self.CentralStack.setFixedWidth(1920)
        self.CentralStack.setFixedHeight(1024)
        self.Setup = Setup()
        self.Program = Program()
        self.CentralStack.addWidget(self.Setup)
        self.CentralStack.addWidget(self.Program)

        # Show setup page
        self.CentralStack.setCurrentIndex(0)
        self.CentralStack.show()

    def app_start(self):
        # First Setup
        self.go_to_setup()

        # Go to Program
        if MasterManager.checkDB():
            QTimer.singleShot(3001, lambda: self.go_to_program())
        else:
            self.Setup.NameSetupPage.nameInput.returnPressed.connect(self.delayed_go_to_program)

    def delayed_go_to_program(self):
        QTimer.singleShot(1001, self.go_to_program)

    def go_to_setup(self):
        self.CentralStack.setCurrentIndex(0)
        self.Setup.start_setup()
    
    def go_to_program(self):
        QTimer.singleShot(2001, lambda: self.Program.ProfilePage.fetchData())
        QTimer.singleShot(2001, lambda: self.Program.DashboardPage.Sidebar.reload())
        QTimer.singleShot(2001, lambda: self.Program.DashboardPage.Todos.fetchPlan())
        QTimer.singleShot(2001, lambda: self.Program.DashboardPage.Journal.initialize())
        QTimer.singleShot(2001, lambda: self.Program.TargetPage.initializeTarget())
        QTimer.singleShot(4001, lambda: self.CentralStack.setCurrentIndex(1))