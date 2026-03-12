import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PySide6.QtCore import Signal

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit_portocale = QLineEdit(placeholderText="Enter kg oranges")
        self.edit_price = QLineEdit(placeholderText="Enter price per kg")
        self.edit_portocale_stricate = QLineEdit(placeholderText="Enter bad oranges kg")
        self.label = QLabel("Results")
        self.button = QPushButton("Calculate")

        layout = QVBoxLayout()
        layout.addWidget(self.edit_portocale)
        layout.addWidget(self.edit_price)
        layout.addWidget(self.edit_portocale_stricate)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.button.clicked.connect(self.calculate)

    def calculate(self):
        x = float(self.edit_portocale.text())
        p = float(self.edit_price.text())
        x_one = float(self.edit_portocale_stricate.text())

        new_price = ((p * x_one) / (x - x_one)) + p

        self.label.setText(f"New price for kg is: {new_price}")




if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())