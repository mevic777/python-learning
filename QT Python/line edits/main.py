# PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Application")
        self.setGeometry(750, 300, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))

        self.line_edit = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)

        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.submit_button.setGeometry(220, 10, 100, 40)

        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Arial;")
        self.submit_button.setStyleSheet("font-size: 18px;"
                                         "font-family: Arial;")
        self.line_edit.setPlaceholderText("Enter your name...")

        self.submit_button.clicked.connect(self.submit)


    def submit(self):
        text = self.line_edit.text()

        print(f"Hello, {text}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show() 
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()