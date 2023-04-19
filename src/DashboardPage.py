from PyQt5.QtWidgets import *

from TodosComponent import *

from SidebarComponent import *
from JournalComponent import *

from SidebarComponent import *
from JournalComponent import *

class DashboardPage(QWidget):
    def __init__(self, parent=None):        
        super(DashboardPage, self).__init__(parent)

        # Load UI
        self.setGeometry(0, 0, 1920, 1024)
        self.setStyleSheet("background-color: rgb(31,31,31);")
        self.lower()

        # Initialize Content
        self.Content = QFrame(self)
        self.Content.setGeometry(0, 0, 1420, 1024)
        self.Content.setStyleSheet("background-color: rgb(31,31,31);")
        self.ContentLayout = QVBoxLayout(self.Content)
        self.Content.setLayout(self.ContentLayout)
        
        # Initialize Sidebar
        self.Sidebar = SidebarComponent(self)

        # Initialize Todos to Content Layout
        self.Todos = TodosComponent(self)
        self.ContentLayout.addWidget(self.Todos)

        # Initialize Journal
        self.Journal = JournalComponent(self)

        self.show()