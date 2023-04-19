import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

from TargetManager import *

class TargetPage(QWidget):
    def __init__(self, parent=None):
        super(TargetPage, self).__init__(parent)
        loadUi('src/uibuilder/Target.ui', self)

        self.countTarget = 0

        # Define fonts
        fontMB = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Bold.otf"))
        fontMM = QFontDatabase.addApplicationFont(os.path.abspath("src/assets/Montserrat-Medium.otf"))
        self.fontFamilyMB = QFontDatabase.applicationFontFamilies(fontMB)[0]
        self.fontFamilyMM = QFontDatabase.applicationFontFamilies(fontMM)[0]

        # Initialize font
        fontTargetLabel = QFont(self.fontFamilyMB, 48, 75, 0)
        fontReachedLabel = QFont(self.fontFamilyMB, 26, 75, 0)
        fontNewTargetButton = QFont(self.fontFamilyMM, 12, 75, 0)

        # Set font
        self.TargetLabel.setFont(fontTargetLabel)
        self.ReachedLabel.setFont(fontReachedLabel)
        self.NewTargetButton.setFont(fontNewTargetButton)
        
        # Set Stylesheet For Inputs
        inputStylesheet = ' color: rgb(129, 129, 129); \
                            padding-left: 10px;      \
                            padding-right: 10px;    \
                            padding-top: 8px;       \
                            padding-bottom: 8px;    \
                            border: 0px;            \
                            border-radius: 10px;    \
                            background-color: rgb(40, 40, 40); \
                            font: 10pt \"' + self.fontFamilyMM + '\";'
        self.InputNewTarget.setStyleSheet(inputStylesheet)
        self.InputYearTarget.setStyleSheet(inputStylesheet)

        # Connect buttons
        self.NewTargetButton.clicked.connect(self.newTargetClicked)
        self.SaveTargetButton.clicked.connect(self.saveTargetClicked)

        # Set Layout Alignment
        self.TargetLayout.setAlignment(Qt.AlignTop)
        self.ReachedList.setAlignment(Qt.AlignTop)
        self.TargetList.setAlignment(Qt.AlignTop)
        self.TargetLayout.setAlignment(self.NewTargetButton, Qt.AlignCenter)
        self.TargetScroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        
        self.ListOfTarget = []
        self.statusInput = 0
        self.statusInputTargetLayout()
        

    def initializeTarget(self):
        # Get all target from database
        self.countTarget = TargetManager.getTargetCountDB()
        targets = TargetManager.getAllTargetDB()
        for target in targets:
            if target[3] == 0:
                self.addTarget(str(target[1]), str(target[2]))
            elif target[3] == 1:
                self.addReachedTarget(str(target[1]), str(target[2]))

    # Hide or Show input target (NewTargetLayout)
    def statusInputTargetLayout(self):
        if self.statusInput == 0:
            self.NewTargetButton.show()
            self.InputNewTarget.hide()
            self.InputYearTarget.hide()
            self.SaveTargetButton.hide()
        else:
            self.NewTargetButton.hide()
            self.InputNewTarget.show()
            self.InputYearTarget.show()
            self.SaveTargetButton.show()

    # Initiate new checkbox
    def initiateNewTarget(self, checkbox: QCheckBox):
        checkbox.setObjectName(str(self.countTarget))
        checkbox.setFixedSize(840, 56)
        checkbox.setCursor(QCursor(Qt.PointingHandCursor))
        checkbox.stateChanged.connect(lambda state: self.checkboxTargetClicked(checkbox, state))
    
    # Initiate new button
    def initiateNewButton(self, val: int):
        newButton = QPushButton()
        newButton.setFixedSize(28, 28)
        newButton.setCursor(QCursor(Qt.PointingHandCursor))
        newButton.setCheckable(True)

        if val == 0:        # Edit Button
            newButton.setStyleSheet('border-image: url(\"src/assets/TargetEditButton.png\"); \
                                    border: none; \
                                    background-repeat: none;')
        else:               # Delete Button
            newButton.setStyleSheet('border-image: url(\"src/assets/TargetDeleteButton.png\"); \
                                    border: none; \
                                    background-repeat: none;')
            
        return newButton

    # Add a new target
    def addTarget(self, text: str, year: str):
        self.countTarget += 1
        # Initiate new checkbox
        checkbox = QCheckBox(text + '  ' + year)
        self.initiateNewTarget(checkbox)
        self.setCheckboxStyleSheet(checkbox, 1)
        
        self.TargetList.addWidget(checkbox)
        self.ListOfTarget.append(checkbox.objectName())

    # add a new reached target
    def addReachedTarget(self, text: str, year: str):
        self.countTarget += 1
        # Initiate new checkbox
        checkbox = QCheckBox(text + '  ' + year)
        self.initiateNewTarget(checkbox)
        self.setCheckboxStyleSheet(checkbox, 0)

        checkbox.setChecked(True)

        self.ReachedList.addWidget(checkbox)
        self.ListOfTarget.append(checkbox.objectName())
        
    # Save Target Button Clicked
    def saveTargetClicked(self):
        self.statusInput = 0
        self.addTarget(self.InputNewTarget.text(), self.InputYearTarget.text())
        self.statusInputTargetLayout()

        # Dynamicaly increase scroll area widget height to adjust scroll bar value
        height = self.TargetScrollWidget.height() + 90
        self.TargetScrollWidget.setFixedHeight(height)

        TargetManager.insertTargetDB(self.InputNewTarget.text(), self.InputYearTarget.text())

        
    # New Target Button Clicked
    def newTargetClicked(self):
        self.statusInput = 1
        self.statusInputTargetLayout()
        
    # Checkbox State Changed
    def checkboxTargetClicked(self, checkbox: QCheckBox, state):
        if state == Qt.CheckState.Checked:
            self.ReachedList.addWidget(checkbox)
            self.setCheckboxStyleSheet(checkbox, 0)
            TargetManager.reachedTargetDB(int(checkbox.objectName()))
        else:
            self.TargetList.addWidget(checkbox)
            self.setCheckboxStyleSheet(checkbox, 1)
            TargetManager.unReachedTargetDB(int(checkbox.objectName()))
    

    def setCheckboxStyleSheet(self, checkbox: QCheckBox, val: int):
        if val == 1:        # Unchecked Stylesheet (Target)
            checkbox.setStyleSheet('QCheckBox \
                                    {color: rgb(220, 220, 220); \
                                    spacing: 12px; \
                                    padding-top: 10px; \
                                    padding-left: 10px; \
                                    padding-bottom: 10px; \
                                    border-bottom: 1px solid; \
                                    border-bottom-color: rgb(190, 190, 190); \
                                    font: 12pt \"' + self.fontFamilyMM + '\";} \
                                QCheckBox::indicator \
                                    {border: 0px; \
                                    width : 20px; \
                                    height : 20px; \
                                    border-radius: 11px;} \
                                QCheckBox::indicator::unchecked \
                                    { \
                                        image: url(./src/assets/UncheckedTarget.png); \
                                    } \
                                QCheckBox::indicator::checked \
                                    { \
                                        image: url(./src/assets/CheckedTarget.png); \
                                    }')
            
        else:               # Checked Stylesheet (Reached)
            checkbox.setStyleSheet('QCheckBox \
                                    {color: rgb(129, 129, 129); \
                                    spacing: 12px; \
                                    padding-top: 10px; \
                                    padding-left: 10px; \
                                    padding-bottom: 10px; \
                                    border-bottom: 1px solid; \
                                    border-bottom-color: rgb(190, 190, 190); \
                                    font: 12pt \"' + self.fontFamilyMM + '\";} \
                                QCheckBox::indicator \
                                    {border: 0px; \
                                    width : 20px; \
                                    height : 20px; \
                                    border-radius: 11px;} \
                                QCheckBox::indicator::unchecked \
                                    { \
                                        image: url(./src/assets/UncheckedTarget.png); \
                                    } \
                                QCheckBox::indicator::checked \
                                    { \
                                        image: url(./src/assets/CheckedTarget.png); \
                                    }')


def main():
    app = QApplication(sys.argv)
    target = TargetPage()
    target.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
