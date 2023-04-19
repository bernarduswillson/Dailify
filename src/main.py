import sys
from PyQt5.QtWidgets import QApplication

import MainWindow as Window

if __name__ == '__main__':
    # Create application
    app = QApplication(sys.argv)

    # Create main window
    window = Window.MainWindow()
    window.setWindowTitle("Dailify")
    window.setFixedHeight(1024)
    window.setFixedWidth(1920)
    window.showMaximized()

    # Start app
    window.app_start()

    sys.exit(app.exec_())