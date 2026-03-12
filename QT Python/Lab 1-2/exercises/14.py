import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PySide6.QtCore import Signal


class FormTwo(QDialog):
    def __init__(self, parent = None):
        super(FormTwo, self).__init__(parent)

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def udpate_label(self, text):
        self.label.setText(text)


class Form(QDialog):
    pass_message = Signal(str)

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit = QLineEdit()
        self.button_one = QPushButton("Show in another window")
        self.button_two = QPushButton("Delete message")
        self.button_three = QPushButton("Close app")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button_one)
        layout.addWidget(self.button_two)
        layout.addWidget(self.button_three)

        self.setLayout(layout)

        self.button_one.clicked.connect(self.show_in_another_window)
        self.button_two.clicked.connect(self.edit.clear)
        self.button_three.clicked.connect(self.close)
    
    def show_in_another_window(self):
        self.w = FormTwo()
        
        self.pass_message.connect(self.w.udpate_label)
        text = self.edit.text()
        self.pass_message.emit(text)
        
        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())