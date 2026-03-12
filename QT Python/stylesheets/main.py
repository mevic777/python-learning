# PyQt5

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Application")
        self.setGeometry(750, 300, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))
        
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        # self.button1.setStyleSheet("font-family: Arial;")

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;            
                margin: 30px;
                border: 3px solid black;
                border-radius: 10px;
            }
                           
            #button1 {
                background-color: red;
            }
            
            #button2 {
                background-color: green;
            }
            
            #button3 {
                background-color: blue;
            }
                           
            QPushButton:hover {
                border-color: yellow;
            }
        """)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show() 
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()