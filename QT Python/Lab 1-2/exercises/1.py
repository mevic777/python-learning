import sys
from PySide6.QtWidgets import QDialog, QApplication, QLineEdit, QPushButton, QVBoxLayout, QLabel

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
    
        self.edit = QLineEdit("Write a name here")
        self.button = QPushButton("Click me")
        self.label = QLabel("Text will appear here")
        
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.button.clicked.connect(self.greeting)

    def greeting(self):
        self.label.setText(f"Hello, {self.edit.text()}")
        print(f"Hello, {self.edit.text()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())