# PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Application")
        self.setGeometry(750, 300, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 18))
        label.setGeometry(0, 0, 500, 100)
        # it uses the CSS code for stylesheet
        label.setStyleSheet("color: blue;" "background: green;" "font-weight: bold;" "font-style: italic;")

        # label.setAlignment(Qt.AlignTop) Vertically
        # label.setAlignment(Qt.AlignBottom) Vertically
        # label.setAlignment(Qt.AlignRight) Horizontally

        # We could combine that with a bit wise or "|"
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) 
        
        label.setAlignment(Qt.AlignCenter)
        # label.setAlignment(Qt.AlignLeft)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show() # it only shows for a couple of seconds
    # but sys.exit() helps us with maintaining the window open until
    sys.exit(app.exec_()) # user do some action on the window

if __name__ == "__main__":
    main()