import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Qt

class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        self.a_edit = QLineEdit()
        self.b_edit = QLineEdit()
        self.button = QPushButton("Calculate")
        self.result = QLabel("Result: ")

        layout = QVBoxLayout()
        layout.addWidget(self.a_edit)
        layout.addWidget(self.b_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        self.setLayout(layout)

        self.button.clicked.connect(self.calculate_inequation)

    def calculate_inequation(self):
        self.result.setText(f"Result: x > {float(self.b_edit.text()) / float(self.a_edit.text())}")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())