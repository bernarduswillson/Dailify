from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

from MasterManager import *
from UserManager import *

from LoadingPage import *
from NameSetupPage import *

class Setup(QWidget):
    def __init__(self, parent=None):
        super(Setup, self).__init__(parent)
        loadUi('src/uibuilder/Setup.ui', self)

        # Initialize Pages
        self.SetupStack = QStackedWidget(self)
        self.SetupStack.setFixedWidth(1920)
        self.SetupStack.setFixedHeight(1024)
        self.LoadingPage = LoadingPage()
        self.NameSetupPage = NameSetupPage()
        self.SetupStack.addWidget(self.LoadingPage)
        self.SetupStack.addWidget(self.NameSetupPage)
        
        # Show intro page
        self.SetupStack.setCurrentIndex(0)
        self.SetupStack.show()
    
    def start_setup(self):
        timer = QTimer(self)
        self.SetupStack.setCurrentIndex(0)

        # Intro page
        self.LoadingPage.intro()

        # Loading page
        timer.singleShot(3001, lambda: self.LoadingPage.loading())

        # If user is undefined, go to name setup page
        if not MasterManager.checkDB():
            # Enter user name
            timer.singleShot(7001, lambda: self.enter())
           
    def enter(self):
        self.SetupStack.setCurrentIndex(1)
        self.NameSetupPage.nameInput.returnPressed.connect(self.onNameInputReturnPressed)
    
    def onNameInputReturnPressed(self):
        self.NameSetupPage.name = self.NameSetupPage.nameInput.text()
        UserManager.insertUser(self.NameSetupPage.name)

        for i in range(1, 1002):
            alpha = i / 1000.0  # Calculate alpha as a float value between 0.001 and 1
            QTimer.singleShot(int(i), lambda a=alpha: self.NameSetupPage.inputLabel.setStyleSheet("color: rgba(143, 115, 101, {});".format(1-a)))
        for i in range(1, 1002):
            alpha = i / 1000.0  # Calculate alpha as a float value between 0.001 and 1
            QTimer.singleShot(int(i), lambda a=alpha: self.NameSetupPage.nameInput.setStyleSheet("background-color: rgba(40, 40, 40, {}); border-radius: 25px; color: rgba(129, 129, 129, {}); padding-left: 30px; margin-left: 500px; margin-right: 500px;".format(1-a, 1-a)))

        # Go to loading after user name input
        QTimer.singleShot(1003, lambda: self.SetupStack.setCurrentIndex(0))
        QTimer.singleShot(1003, lambda: self.LoadingPage.loading())


