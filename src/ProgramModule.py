from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

# from Navbar import *
from NavTop import *
from NavSide import *
from DashboardPage import *
from ProfilePage import *
from TargetPage import *
from JournalManager import *

class Program(QWidget):
    def __init__(self, parent=None):
        super(Program, self).__init__(parent)
        loadUi('src/uibuilder/Program.ui', self)

        # Initialize Navbar
        # self.Navbar = Navbar(self)
        # self.Navbar.DashboardBtn.clicked.connect(self.go_to_dashboard)
        # self.Navbar.TargetBtn.clicked.connect(self.go_to_target)
        # self.Navbar.ProfileBtn.clicked.connect(self.go_to_profile)

        # Initialize Navbar 2
        self.NavSide = NavSide(self)
        self.NavSide.move(-310, 0)
        self.NavSide.setStyleSheet("background-color: rgb(41,41,41)")
        self.NavTop = NavTop(self)
        self.NavTop.setStyleSheet("background-color: rgb(41,41,41)")
        self.NavTop.MenuBtn.clicked.connect(self.toggleMenu)
        self.NavSide.DashboardBtn.clicked.connect(self.go_to_dashboard)
        self.NavSide.TargetBtn.clicked.connect(self.go_to_target)
        self.NavSide.ProfileBtn.clicked.connect(self.go_to_profile)

        # Initialize Pages
        self.ProgramStack = QStackedWidget(self)
        self.ProgramStack.setFixedWidth(1920)
        self.ProgramStack.setFixedHeight(1024)
        self.ProgramStack.lower()
        self.ProgramStack.setStyleSheet("background-color: rgb(31, 31 , 31);")

        self.DashboardPage = DashboardPage(self)
        self.TargetPage = TargetPage()
        # self.TargetPage = TargetPage()
        self.ProfilePage = ProfilePage()
        
        self.ProgramStack.addWidget(self.DashboardPage)
        self.ProgramStack.addWidget(self.TargetPage)
        self.ProgramStack.addWidget(self.ProfilePage)

        # Stylsheet State
        self.active = "QPushButton{color:rgb(190,190,190); background-color: rgb(51,51,51); border: none;padding-left: 20px;text-align: left;} QPushButton:hover {background-color: rgb(51,51,51);}"
        self.inactive = "QPushButton{color:rgb(190,190,190); border: none;padding-left: 20px;text-align: left;} QPushButton:hover {background-color: rgb(51,51,51);}"

        # Stylsheet State
        self.active = "QPushButton{color:rgb(190,190,190); background-color: rgb(51,51,51); border: none;padding-left: 20px;text-align: left;} QPushButton:hover {background-color: rgb(51,51,51);}"
        self.inactive = "QPushButton{color:rgb(190,190,190); border: none;padding-left: 20px;text-align: left;} QPushButton:hover {background-color: rgb(51,51,51);}"

        # Show dashboard page
        self.ProgramStack.setCurrentIndex(0)
        self.NavTop.DashboardLabel.show()
        self.NavSide.DashboardBtn.setStyleSheet(self.active)
        self.NavSide.TargetBtn.setStyleSheet(self.inactive)
        self.NavSide.ProfileBtn.setStyleSheet(self.inactive)
        self.show()
    
    def go_to_dashboard(self):
        self.NavTop.DashboardLabel.show()
        self.NavSide.DashboardBtn.setStyleSheet(self.active)
        self.NavSide.TargetBtn.setStyleSheet(self.inactive)
        self.NavSide.ProfileBtn.setStyleSheet(self.inactive)
        self.ProgramStack.setCurrentIndex(0)
        self.closeMenu()
        
    def go_to_target(self):
        self.NavTop.DashboardLabel.hide()
        self.NavSide.DashboardBtn.setStyleSheet(self.inactive)
        self.NavSide.TargetBtn.setStyleSheet(self.active)
        self.NavSide.ProfileBtn.setStyleSheet(self.inactive)
        self.ProgramStack.setCurrentIndex(1)
        self.closeMenu()
    
    def go_to_profile(self):
        self.NavTop.DashboardLabel.hide()
        self.NavSide.DashboardBtn.setStyleSheet(self.inactive)
        self.NavSide.TargetBtn.setStyleSheet(self.inactive)
        self.NavSide.ProfileBtn.setStyleSheet(self.active)
        self.ProgramStack.setCurrentIndex(2)

        self.ProfilePage.user.setCreatedJournals(JournalManager.countJournal())
        self.ProfilePage.fetchData()
        self.closeMenu()

    def toggleMenu(self):
        if self.NavSide.pos().x() == 0:
            self.closeMenu()
        else:
            self.openMenu()
    
    def openMenu(self):
        self.animation = QPropertyAnimation(self.NavSide, b"pos") 
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(-310, 0))
        self.animation.setEndValue(QPoint(0,0))
        self.animation.setDuration(200)
        self.animation.start()
    
    def closeMenu(self):
        self.animation = QPropertyAnimation(self.NavSide, b"pos") 
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QPoint(0, 0))
        self.animation.setEndValue(QPoint(-310,0))
        self.animation.setDuration(200)
        self.animation.start()
