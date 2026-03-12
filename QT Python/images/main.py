# PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Application")
        self.setGeometry(750, 300, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("icon.png")

        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry((self.width() - label.width()) // 2, (self.height() - label.height()) // 2, label.width(), label.height())

        

        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show() 
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()