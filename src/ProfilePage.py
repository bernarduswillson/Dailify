from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import os

from MasterManager import *
from UserManager import *

from Entity.User import *

class ProfilePage(QWidget):
    def __init__(self, parent=None):
        super(ProfilePage, self).__init__(parent)
        loadUi('src/uibuilder/ProfilePage.ui', self)

        # Fonts
        fontMB = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Bold.otf"))
        fontMM = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Medium.otf"))
        self.fontFamilyMB = QFontDatabase.applicationFontFamilies(fontMB)[0]
        self.fontFamilyMM = QFontDatabase.applicationFontFamilies(fontMM)[0]

        self.ProfileHeader.setFont(QFont(self.fontFamilyMB, 48, 75))
        self.NameLabel.setFont(QFont(self.fontFamilyMM, 13))
        self.NameData.setFont(QFont(self.fontFamilyMM, 13))
        self.UTodosLabel.setFont(QFont(self.fontFamilyMM, 13))
        self.UTodosData.setFont(QFont(self.fontFamilyMM, 13))
        self.UTargetsLabel.setFont(QFont(self.fontFamilyMM, 13))
        self.UTargetsData.setFont(QFont(self.fontFamilyMM, 13))
        self.RTargetsLabel.setFont(QFont(self.fontFamilyMM, 13))
        self.RTargetsData.setFont(QFont(self.fontFamilyMM, 13))
        self.JournalsLabel.setFont(QFont(self.fontFamilyMM, 13))
        self.JournalsData.setFont(QFont(self.fontFamilyMM, 13))

        # Fetch data from database
        if MasterManager.checkDB():
            self.fetchData()

        # Connect buttons
        self.NameEditBtn.clicked.connect(self.editName)

    def fetchData(self):
        self.user = User(UserManager.getUser())
        self.ProfileHeader.setText(f"{self.user.getName()}'s Profile")
        self.NameData.setText(f"{self.user.getName()}")
        self.UTodosData.setText(f"{str(self.user.getUncompletedTodos())}")
        self.UTargetsData.setText(f"{str(self.user.getUnreachedTargets())}")
        self.RTargetsData.setText(f"{str(self.user.getReachedTargets())}")
        self.JournalsData.setText(f"{str(self.user.getCreatedJournals())}")
    
    def editName(self):
        self.NameData.setEnabled(True)
        self.NameData.setFocus()

        self.NameData.returnPressed.connect(self.updateName)
        self.NameData.editingFinished.connect(self.updateName)
    
    def updateName(self):
        self.user.setName(self.NameData.text())
        UserManager.updateUser(0, self.user)
        self.fetchData()
        self.NameData.setEnabled(False)
        
