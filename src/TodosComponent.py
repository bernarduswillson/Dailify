from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import datetime

from PlanManager import *
from TodoManager import *

from Entity.Todo import *

from TodoList import *  

class TodosComponent(QWidget):
    def __init__(self, parent=None):
        super(TodosComponent, self).__init__(parent)
        loadUi('src/uibuilder/TodosComponent.ui', self)

        # Connect buttons
        self.NewTodoBtn.clicked.connect(self.showTodoForm)
        self.SaveBtn.clicked.connect(self.saveTodo)

        # Initialize local variables
        self.initLocalVariable()

        # Initialize empty label
        if self.plan["plan_id"] == None:
            self.EmptyLabel.show()
        else:
            self.EmptyLabel.hide()

        self.hideInvalidMsg()
        self.hideTodoForm()
        self.show()

    def initLocalVariable(self):
        self.plan = {
            "current_date" : self.parent().Sidebar.selectedDate,
            "plan_id" : None,
            "todos" : [],
        }
    
    def updateTodosList(self):
        while self.TodosLayout.count():
            child_widget = self.TodosLayout.takeAt(0).widget()
            child_widget.setParent(None)
        for todo in self.plan["todos"]:
            self.TodosLayout.addWidget(TodoList(todo.getContent(), todo.getStart(), todo.getEnd(), self))

    def fetchPlan(self):
        self.plan["todos"] = []
        self.plan["plan_id"] = PlanManager.getPlanId(self.plan["current_date"].toString("yyyy-MM-dd"))
        for todos in TodoManager.getPlanTodos(self.plan["plan_id"]):
            todo = Todo(todos[1], todos[2], todos[3], todos[4], todos[5])
            self.plan["todos"].append(todo)
        self.updateTodosList()
        print(self.plan["todos"])
    
    def showTodoForm(self):
        self.NewTodoBtn.hide()
        self.StartInput.show()
        self.EndInput.show()
        self.NameInput.show()
        self.SaveBtn.show()
    
    def hideTodoForm(self):
        self.NewTodoBtn.show()
        self.StartInput.hide()
        self.EndInput.hide()
        self.NameInput.hide()
        self.SaveBtn.hide()
    
    def resetTodoForm(self):
        self.InvalidMsg.setText("")
        self.StartInput.setText("")
        self.EndInput.setText("")
        self.NameInput.setText("")

    def hideInvalidMsg(self):
        self.InvalidMsg.setText("")
        self.InvalidMsg.setStyleSheet("QLabel {color: rgb(220,220,220);background-color: rgb(31,31,31);border-radius: 10px;}")

    def showInvalidMsg(self, msg):
        self.InvalidMsg.setText(msg)
        self.InvalidMsg.setStyleSheet("QLabel {color: rgb(220,220,220);background-color: rgb(220,90,90);border-radius: 10px;}")

    def validateForm(self):
        if len(self.NameInput.text()) == 0 or self.NameInput.text().isspace():
            self.showInvalidMsg("Your todo must have a name")
            return False
        
        startSec = 0
        if len(self.StartInput.text()) != 0 and not self.StartInput.text().isspace():
            if self.StartInput.text().count('.') == 1:
                startInputArr = self.StartInput.text().split('.')
                if startInputArr[0].isnumeric() and startInputArr[0].isnumeric():
                    if 0 <= int(startInputArr[0]) < 24 and 0 <= int(startInputArr[1]) < 60:
                        startSec = int(startInputArr[0]) * 3600 + int(startInputArr[1]) * 60
                    else:
                        self.showInvalidMsg("Make sure the start time is in the right format")
                        return False
                else:
                    self.showInvalidMsg("Make sure the start time is in the right format")
                    return False
            else:
                self.showInvalidMsg("Make sure the start time is in the right format")
                return False
        
        if len(self.EndInput.text()) != 0 and not self.EndInput.text().isspace() and len(self.StartInput.text()) != 0 and not self.StartInput.text().isspace():
            if self.EndInput.text().count('.') == 1:
                EndInputArr = self.EndInput.text().split('.')
                if EndInputArr[0].isnumeric() and EndInputArr[0].isnumeric():
                    if 0 <= int(EndInputArr[0]) < 24 and 0 <= int(EndInputArr[1]) < 60:
                        if int(EndInputArr[0]) * 3600 + int(EndInputArr[1]) * 60 < startSec:
                            self.showInvalidMsg("Start time cannot be later than end time")
                            return False 
                    else:
                        self.showInvalidMsg("Make sure the end time is in the right format")
                        return False 
                else:
                    self.showInvalidMsg("Make sure the end time is in the right format")
                    return False
            else:
                self.showInvalidMsg("Make sure the end time is in the right format")
                return False
        elif len(self.EndInput.text()) != 0 and not self.EndInput.text().isspace() and (len(self.StartInput.text()) == 0 or self.StartInput.text().isspace()):
            self.showInvalidMsg("Start time cannot be empty")
            return False 
            
        return True

    def saveTodo(self):
        if self.validateForm():
            self.hideInvalidMsg()
            self.hideTodoForm()
            if not PlanManager.checkPlan(self.plan["current_date"].toString("yyyy-MM-dd")):
                PlanManager.createPlan(self.plan["current_date"].toString("yyyy-MM-dd"))
            self.plan["plan_id"] = PlanManager.getPlanId(self.plan["current_date"].toString("yyyy-MM-dd"))
            newTodo = Todo(self.plan["plan_id"],self.NameInput.text(),self.StartInput.text(),self.EndInput.text(),False)
            TodoManager.createTodo(newTodo) 
            self.resetTodoForm()
            self.fetchPlan()
            self.updateTodosList()
    
    def deleteTodo(self, id):
        TodoManager.deleteTodo(id)
        self.fetchPlan()
        self.updateTodosList()
