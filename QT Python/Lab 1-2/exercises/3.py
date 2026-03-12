import sys
from PySide6.QtWidgets import QDialog, QApplication, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QFont

class Form(QDialog):
    
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        
        self.label = QLabel("Text")
        self.button1 = QPushButton("Bigger")
        self.button2 = QPushButton("Smaller")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        
        self.setLayout(layout)
        
        self.button1.clicked.connect(self.make_text_bigger)
        self.button2.clicked.connect(self.make_text_smaller)

        self.font_size = 14
        self.update_font()
        
    def make_text_bigger(self):
        self.font_size += 2
        self.update_font()
        
    def make_text_smaller(self):
        self.font_size -= 2
        self.update_font()
        
    def update_font(self):
        font = QFont()
        font.setPointSize(self.font_size)
        self.label.setFont(font)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())