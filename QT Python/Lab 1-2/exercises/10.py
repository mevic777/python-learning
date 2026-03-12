import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import Qt

class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        self.button = QPushButton("Make text big")
        self.edit = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.button.clicked.connect(self.transform_upper)

    def transform_upper(self):
        self.edit.setText(self.edit.text().upper())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())