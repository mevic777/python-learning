# PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Application")
        self.setGeometry(750, 300, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show() # it only shows for a couple of seconds
    # but sys.exit() helps us with maintaining the window open until
    sys.exit(app.exec_()) # user do some action on the window

if __name__ == "__main__":
    main()