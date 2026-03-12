import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PySide6.QtCore import Signal

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit_one = QLineEdit(placeholderText="Expression")

        self.button_one = QPushButton("Calculate")

        self.result_label = QLabel("Result will appear here")

        layout = QVBoxLayout()

        layout.addWidget(self.edit_one)
        layout.addWidget(self.button_one)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        self.button_one.clicked.connect(self.calculate)
    
    def calculate(self):
        self.result_label.setText(f"Result is: {eval(self.edit_one.text())}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())