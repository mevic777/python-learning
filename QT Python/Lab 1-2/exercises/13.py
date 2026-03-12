import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel, QPushButton, QLineEdit
import math


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit = QLineEdit()
        self.edit_one = QLineEdit()
        self.button = QPushButton("Rastoarna cuvantul")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.edit_one)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.rastoarna)

    def rastoarna(self):
        self.edit_one.setText(self.edit.text()[::-1])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())