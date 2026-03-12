import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Qt

class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        self.edit = QLineEdit()
        self.button1 = QPushButton("Rosu")
        self.button2 = QPushButton("Galben")
        self.button3 = QPushButton("Verde")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

        self.button1.clicked.connect(self.make_text_red)
        self.button2.clicked.connect(self.make_text_yellow)
        self.button3.clicked.connect(self.make_text_green)

    def make_text_red(self):
        self.edit.setStyleSheet("color: red;")
    
    def make_text_yellow(self):
        self.edit.setStyleSheet("color: yellow;")

    def make_text_green(self):
        self.edit.setStyleSheet("color: green;")
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())