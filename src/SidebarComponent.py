from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import sqlite3

from TipsManager import *


class SidebarComponent(QFrame):
    def __init__ (self, parent=None):
        super(SidebarComponent, self).__init__(parent)

        fontMB = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Bold.otf"))
        fontMM = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Medium.otf"))
        self.fontFamilyMB = QFontDatabase.applicationFontFamilies(fontMB)[0]
        self.fontFamilyMM = QFontDatabase.applicationFontFamilies(fontMM)[0]

        self.setStyleSheet("background-color: rgba(40,40,40,1);")
        self.setGeometry(1420, 0, 500, 1080)

        self.prevID = 0
        self.selectedDate = QDate.currentDate()
    
        self.showCalendar()
        self.showTips()


    def showCalendar(self):
        fontDate = QFont(self.fontFamilyMB, 70, 75)

        self.date = QLabel(str(QDate.currentDate().toString("dd")), self)
        self.date.setGeometry(0, 95, 500, 150)
        self.date.setAlignment(Qt.AlignCenter)
        self.date.setStyleSheet("color : rgb(255, 255, 255); color: rgb(143, 115, 101) ; background-color: rgba(255,255,255,0);")
        self.date.setFont(fontDate)

        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(50, 260, 400, 300)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
        self.calendar.setStyleSheet(
            "background-color: rgb(40,40,40); color: rgb(180,180,180); font: 12pt 'Montserrat Medium';"
            "selection-background-color: rgb(220,220,220); selection-color: rgb(40,40,40);"
        )
        self.calendar.setWindowFlags(Qt.FramelessWindowHint)

        self.calendar.selectionChanged.connect(self.updateDateLabel)
        self.calendar.selectionChanged.connect(self.updateJournal)
        self.calendar.selectionChanged.connect(self.updateTodos)

    def showTips(self) :
        self.line = QFrame(self)
        self.line.setGeometry(50, 645, 400, 1)
        self.line.setStyleSheet("background-color: white;")
        
        fontHeader = QFont(self.fontFamilyMB, 48, 75)
        fontQuotes = QFont(self.fontFamilyMM, 12)

        self.Header = QLabel(',,',self)
        self.Header.setFont(fontHeader)
        self.Header.setGeometry(230, 615, 50, 100)
        self.Header.setStyleSheet("color : rgb(143, 115, 101); background-color: rgba(40,40,40,0);")

        self.Quotes = QLabel('', self)
        self.Quotes.setWordWrap(True)
        self.Quotes.setAlignment(Qt.AlignCenter)
        self.Quotes.setFont(fontQuotes)
        self.Quotes.setGeometry(50, 740, 400, 180)
        self.Quotes.setStyleSheet("color : rgb(255, 255, 255); background-color: rgba(255,255,255,0)")

        self.Reload = QPushButton('', self)
        self.Reload.setGeometry(196, 950, 108, 32)
        self.Reload.setStyleSheet("background-image: url(src/assets/reload.png); background-repeat: no-repeat; border: none;")
        self.Reload.setCursor(QCursor(Qt.PointingHandCursor))
        self.Reload.clicked.connect(self.reload)

    def reload(self):
        QuoteData = TipsManager.getRandomQuote(self.prevID)
        self.prevID = QuoteData[0]
        quote = QuoteData[1]
        self.Quotes.setText(quote)

    def updateDateLabel(self):
        self.selectedDate = self.calendar.selectedDate()
        # cara akses tanggal, bulan, tahun
        # print(self.selectedDate.toString("yy"))
        # print(self.selectedDate.toString("mm"))
        # print(self.selectedDate.toString("dd"))
        selectedDate = self.calendar.selectedDate().toString("dd")
        self.date.setText(selectedDate)

    # every time the calendar is clicked, the journal will be updated
    def updateJournal(self):
        self.selectedDate = self.calendar.selectedDate()
        self.parent().Journal.loadJournal(self.selectedDate.toString("yyyy-MM-dd"))
    
    def updateTodos(self):
        self.selectedDate = self.calendar.selectedDate()
        self.parent().Todos.plan["current_date"] = self.selectedDate
        self.parent().Journal.loadJournal(self.selectedDate.toString("yyyy-MM-dd"))
