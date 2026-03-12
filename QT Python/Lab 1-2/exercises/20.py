import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PySide6.QtCore import Signal

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit_one = QLineEdit(placeholderText="Numarul zilei din saptamana")
        self.edit_two = QLineEdit(placeholderText="Numarul zile din an")
        self.button = QPushButton("Calculate")
        self.label = QLabel("Results")

        layout = QVBoxLayout()
        layout.addWidget(self.edit_one)
        layout.addWidget(self.edit_two)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.button.clicked.connect(self.calculate)

    def calculate(self):
        self.label.setText(f"Apartine la {((int(self.edit_one.text()) + int(self.edit_two.text()) - 2) // 7) + 1} saptamana")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())