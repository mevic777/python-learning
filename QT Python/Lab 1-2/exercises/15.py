import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PySide6.QtCore import Signal

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit = QLineEdit()
        self.button_one = QPushButton("Button 1")
        self.button_two = QPushButton("Button 2")
        self.button_three = QPushButton("Button 3")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button_one)
        layout.addWidget(self.button_two)
        layout.addWidget(self.button_three)

        self.setLayout(layout)

        self.button_one.clicked.connect(self.mButton_one)
        self.button_two.clicked.connect(self.mButton_two)
        self.button_three.clicked.connect(self.mButton_three)

    def mButton_one(self):
        self.edit.setText("First button was pressed")
    
    def mButton_two(self):
        self.edit.setText("Second button was pressed")
    
    def mButton_three(self):
        self.edit.deleteLater()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())