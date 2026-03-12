# PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Application")
        self.setGeometry(750, 300, 500, 500)
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("Mastercard", self)
        self.radio3 = QRadioButton("Gift card", self)
        self.radio4 = QRadioButton("In-store", self)
        self.radio5 = QRadioButton("Online", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.setWindowIcon(QIcon("icon.png"))
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(10, 0, 300, 50)
        self.radio2.setGeometry(10, 50, 300, 50)
        self.radio3.setGeometry(10, 100, 300, 50)
        self.radio4.setGeometry(10, 150, 300, 50)
        self.radio5.setGeometry(10, 200, 300, 50)

        self.setStyleSheet("QRadioButton{" 
        "font-size: 40px;}" 
        "font-family: Arial;" 
        "padding: 20px;")

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_change)
        self.radio2.toggled.connect(self.radio_button_change)
        self.radio3.toggled.connect(self.radio_button_change)
        self.radio4.toggled.connect(self.radio_button_change)
        self.radio5.toggled.connect(self.radio_button_change)

    def radio_button_change(self):
        radio_button = self.sender() # return the widget that sended the signal
        
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show() 
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()