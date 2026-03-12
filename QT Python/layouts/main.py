# PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Application")
        self.setGeometry(750, 300, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background: red;")
        label2.setStyleSheet("background: blue;")
        label3.setStyleSheet("background: green;")
        label4.setStyleSheet("background: yellow;")
        label5.setStyleSheet("background: purple;")

        # vbox = QVBoxLayout()

        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # central_widget.setLayout(vbox)

        # hbox = QHBoxLayout()

        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)

        # central_widget.setLayout(hbox)

        grid = QGridLayout()

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 0, 2)
        grid.addWidget(label4, 1, 0)
        grid.addWidget(label5, 1, 1)

        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show() 
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()