import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Qt

class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        self.button = QPushButton("Square")
        self.edit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.button.clicked.connect(self.square_number)

    def square_number(self):
        n = pow(int(self.edit.text()), 2)
        self.edit.setText(str(n))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())