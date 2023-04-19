from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class TodoList(QWidget):
    def __init__(self, name, start, end, parent = None):
        super(TodoList, self).__init__(parent)
        loadUi('src/uibuilder/TodoList.ui', self)

        self.NameLabel.setText(name)
        if start == None or start == "":
            self.StartLabel.hide()
        self.StartLabel.setText(str(start))
        if end == None or end == "":
            self.EndLabel.hide()
        self.EndLabel.setText(str(end))

        # connect buttons
        # self.EditBtn.clicked.connect(self.parent().deleteTodo(self.id))