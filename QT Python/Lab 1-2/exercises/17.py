import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PySide6.QtCore import Signal

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit_one = QLineEdit(placeholderText="m1 + m2")
        self.edit_two = QLineEdit(placeholderText="m1 + m2 + ... + mn")
        self.edit_three = QLineEdit(placeholderText="m1 +- m2 +- ... +- mn")
        self.edit_four = QLineEdit(placeholderText="m1 * m2")
        self.edit_five = QLineEdit(placeholderText="m1 / m2")

        self.button_one = QPushButton("Calculate")
        self.button_two = QPushButton("Calculate")
        self.button_three = QPushButton("Calculate")
        self.button_four = QPushButton("Calculate")
        self.button_five = QPushButton("Calculate")

        self.result_label = QLabel("Result will appear here")

        layout = QVBoxLayout()

        layout.addWidget(self.edit_one)
        layout.addWidget(self.button_one)

        layout.addWidget(self.edit_two)
        layout.addWidget(self.button_two)

        layout.addWidget(self.edit_three)
        layout.addWidget(self.button_three)

        layout.addWidget(self.edit_four)
        layout.addWidget(self.button_four)

        layout.addWidget(self.edit_five)
        layout.addWidget(self.button_five)

        layout.addWidget(self.result_label)

        self.setLayout(layout)

        self.button_one.clicked.connect(lambda: self.calculate(self.edit_one))
        self.button_two.clicked.connect(lambda: self.calculate(self.edit_two))
        self.button_three.clicked.connect(lambda: self.calculate(self.edit_three))
        self.button_four.clicked.connect(lambda: self.calculate(self.edit_four))
        self.button_five.clicked.connect(lambda: self.calculate(self.edit_five))
    
    def calculate(self, edit):
        try:
            expression = edit.text()
            result = eval(expression)
            self.result_label.setText(f"Result is: {result}")
        except:
            self.result_label.setText("Not such expression")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())