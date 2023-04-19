from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import os
import sys

from JournalManager import *
from SidebarComponent import *

class JournalComponent(QWidget):
    def __init__(self, parent = None):
        super(JournalComponent, self).__init__(parent)
        loadUi("src/uibuilder/Journal.ui", self)

        # access selectedDate from SidebarComponent attribute
        date = self.parent().Sidebar.selectedDate
        # print(date.toString("yyyy-MM-dd"))

        self.date = date.toString("yyyy-MM-dd")

        # Initialize Components
        self.setGeometry(0, 500, 1500, 1000)

        # Font
        fontMB = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Bold.otf"))
        fontMM = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Medium.otf"))
        self.fontFamilyMB = QFontDatabase.applicationFontFamilies(fontMB)[0]
        self.fontFamilyMM = QFontDatabase.applicationFontFamilies(fontMM)[0]

        self.JournalLabel.setFont(QFont(self.fontFamilyMB, 30, 75))
        self.star1.setStyleSheet("image: url(src/assets/StarDown.png);")
        self.star2.setStyleSheet("image: url(src/assets/StarDown.png);")
        self.star3.setStyleSheet("image: url(src/assets/StarDown.png);")
        self.star4.setStyleSheet("image: url(src/assets/StarDown.png);")
        self.star5.setStyleSheet("image: url(src/assets/StarDown.png);")

        self.emot1.setStyleSheet("image: url(src/assets/happyDark.png);")
        self.emot2.setStyleSheet("image: url(src/assets/sadDark.png);")
        self.emot3.setStyleSheet("image: url(src/assets/loveDark.png);")
        self.emot4.setStyleSheet("image: url(src/assets/angryDark.png);")
        self.emot5.setStyleSheet("image: url(src/assets/deadDark.png);")
        self.star1.clicked.connect(self.star1Edit)
        self.star2.clicked.connect(self.star2Edit)
        self.star3.clicked.connect(self.star3Edit)
        self.star4.clicked.connect(self.star4Edit)
        self.star5.clicked.connect(self.star5Edit)
        self.emot1.clicked.connect(self.emot1Edit)
        self.emot2.clicked.connect(self.emot2Edit)
        self.emot3.clicked.connect(self.emot3Edit)
        self.emot4.clicked.connect(self.emot4Edit)
        self.emot5.clicked.connect(self.emot5Edit)

    def initialize(self):
        #semua yang "2020-12-12" diubah ke date.now() make return yang calendar
        self.loadJournal(self.date)
        self.loadRate(self.date)
        self.loademot(self.date)
        self.path = JournalManager.getPath(self.date)
        self.journalBox.textChanged.connect(self.saveJournal)

    def loademot(self, date):
        self.emot1.setStyleSheet("image: url(src/assets/happyDark.png);")
        self.emot2.setStyleSheet("image: url(src/assets/sadDark.png);")
        self.emot3.setStyleSheet("image: url(src/assets/loveDark.png);")
        self.emot4.setStyleSheet("image: url(src/assets/angryDark.png);")
        self.emot5.setStyleSheet("image: url(src/assets/deadDark.png);")
        temp=JournalManager.getMood(self.date)
        if temp==1:
            self.emot1.setStyleSheet("image: url(src/assets/happy.png);")
        elif temp==2:
            self.emot2.setStyleSheet("image: url(src/assets/sad.png);")
        elif temp==3:
            self.emot3.setStyleSheet("image: url(src/assets/love.png);")
        elif temp==4:
            self.emot4.setStyleSheet("image: url(src/assets/angry.png);")
        elif temp==5:
            self.emot5.setStyleSheet("image: url(src/assets/dead.png);")
    
    def emot1Edit(self):
        if JournalManager.getMood(self.date)==1:
            self.emot1.setStyleSheet("image: url(src/assets/happyDark.png);")
            JournalManager.saveMood(self.date,0)
        else:
            self.emot1.setStyleSheet("image: url(src/assets/happy.png);")
            self.emot2.setStyleSheet("image: url(src/assets/sadDark.png);")
            self.emot3.setStyleSheet("image: url(src/assets/loveDark.png);")
            self.emot4.setStyleSheet("image: url(src/assets/angryDark.png);")
            self.emot5.setStyleSheet("image: url(src/assets/deadDark.png);")
            JournalManager.saveMood(self.date,1)
    
    def emot2Edit(self):
        if JournalManager.getMood(self.date)==2:
            self.emot2.setStyleSheet("image: url(src/assets/sadDark.png);")
            JournalManager.saveMood(self.date,0)
        else:
            self.emot1.setStyleSheet("image: url(src/assets/happyDark.png);")
            self.emot2.setStyleSheet("image: url(src/assets/sad.png);")
            self.emot3.setStyleSheet("image: url(src/assets/loveDark.png);")
            self.emot4.setStyleSheet("image: url(src/assets/angryDark.png);")
            self.emot5.setStyleSheet("image: url(src/assets/deadDark.png);")
            JournalManager.saveMood(self.date,2)
    
    def emot3Edit(self):
        if JournalManager.getMood(self.date)==3:
            self.emot3.setStyleSheet("image: url(src/assets/loveDark.png);")
            JournalManager.saveMood(self.date,0)
        else:
            self.emot1.setStyleSheet("image: url(src/assets/happyDark.png);")
            self.emot2.setStyleSheet("image: url(src/assets/sadDark.png);")
            self.emot3.setStyleSheet("image: url(src/assets/love.png);")
            self.emot4.setStyleSheet("image: url(src/assets/angryDark.png);")
            self.emot5.setStyleSheet("image: url(src/assets/deadDark.png);")
            JournalManager.saveMood(self.date,3)
    
    def emot4Edit(self):
        if JournalManager.getMood(self.date)==4:
            self.emot4.setStyleSheet("image: url(src/assets/angryDark.png);")
            JournalManager.saveMood(self.date,0)
        else:
            self.emot1.setStyleSheet("image: url(src/assets/happyDark.png);")
            self.emot2.setStyleSheet("image: url(src/assets/sadDark.png);")
            self.emot3.setStyleSheet("image: url(src/assets/loveDark.png);")
            self.emot4.setStyleSheet("image: url(src/assets/angry.png);")
            self.emot5.setStyleSheet("image: url(src/assets/deadDark.png);")
            JournalManager.saveMood(self.date,4)
    
    def emot5Edit(self):
        if JournalManager.getMood(self.date)==5:
            self.emot5.setStyleSheet("image: url(src/assets/deadDark.png);")
            JournalManager.saveMood(self.date,0)
        else:
            self.emot1.setStyleSheet("image: url(src/assets/happyDark.png);")
            self.emot2.setStyleSheet("image: url(src/assets/sadDark.png);")
            self.emot3.setStyleSheet("image: url(src/assets/loveDark.png);")
            self.emot4.setStyleSheet("image: url(src/assets/angryDark.png);")
            self.emot5.setStyleSheet("image: url(src/assets/dead.png);")
            JournalManager.saveMood(self.date,5)

    def star1Edit(self):
        if JournalManager.getRate(self.date)==1:
            self.star1.setStyleSheet("image: url(src/assets/StarDown.png);")
            JournalManager.saveRate(self.date,0)
        else:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star4.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star5.setStyleSheet("image: url(src/assets/StarDown.png);")
            JournalManager.saveRate(self.date, 1)
        
    def star2Edit(self):
        if JournalManager.getRate(self.date)==2:
            self.star1.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarDown.png);")
            JournalManager.saveRate(self.date,0)
        else:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star4.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star5.setStyleSheet("image: url(src/assets/StarDown.png);")
            JournalManager.saveRate(self.date,2)

    def star3Edit(self):
        if JournalManager.getRate(self.date)==3:
            self.star1.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarDown.png);")
            JournalManager.saveRate(self.date,0)
        else:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star4.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star5.setStyleSheet("image: url(src/assets/StarDown.png);")
            JournalManager.saveRate(self.date,3)

    def star4Edit(self):
        if JournalManager.getRate(self.date)==4:
            self.star1.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star4.setStyleSheet("image: url(src/assets/StarDown.png);")
            JournalManager.saveRate(self.date,0)
        else:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star4.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star5.setStyleSheet("image: url(src/assets/StarDown.png);")
            JournalManager.saveRate(self.date,4)
    
    def star5Edit(self):
        if JournalManager.getRate(self.date)==5:
            self.star1.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star4.setStyleSheet("image: url(src/assets/StarDown.png);")
            self.star5.setStyleSheet("image: url(src/assets/StarDown.png);")
            JournalManager.saveRate(self.date,0)
        else:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star4.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star5.setStyleSheet("image: url(src/assets/StarUp.png);")
            JournalManager.saveRate(self.date,5)

    def loadRate(self,date):
        temp=JournalManager.getRate(date)
        self.star1.setStyleSheet("image: url(src/assets/StarDown.png);")
        self.star2.setStyleSheet("image: url(src/assets/StarDown.png);")
        self.star3.setStyleSheet("image: url(src/assets/StarDown.png);")
        self.star4.setStyleSheet("image: url(src/assets/StarDown.png);")
        self.star5.setStyleSheet("image: url(src/assets/StarDown.png);")
        if temp == 1:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
        elif temp == 2:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarUp.png);")
        elif temp == 3:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarUp.png);")
        elif temp == 4:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star4.setStyleSheet("image: url(src/assets/StarUp.png);")
        elif temp == 5:
            self.star1.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star2.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star3.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star4.setStyleSheet("image: url(src/assets/StarUp.png);")
            self.star5.setStyleSheet("image: url(src/assets/StarUp.png);")

    def saveJournal(self):
        self.path = JournalManager.getPath(self.date)
        self.save(str(self.path))

    def save(self, filename):
        # Get the current content of the QTextEdit widget
        content = self.journalBox.toPlainText()
        # Save the content to a file
        with open(filename, "w") as file:
            file.write(content)
            file.close()

    def loadJournal(self,date):
        self.date = date
        if JournalManager.checkJournal(date):
            filename = JournalManager.getPath(date)
            with open(filename, "r") as file:
                content = file.read()
                self.journalBox.setText(content)
                file.close()
        else:
            JournalManager.createJournal(date)
            self.journalBox.setText("")
        self.loadRate(date)
        self.loademot(date)
            




# def main():
#     app = QApplication(sys.argv)
#     date="2020-12-12"
#     journal = Journal(date)
#     journal.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()