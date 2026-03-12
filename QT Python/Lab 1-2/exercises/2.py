import sys
from PySide6.QtWidgets import QDialog, QApplication, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import Signal


class SecondForm(QDialog):
    result_signal = Signal(int)
    
    def __init__(self, parent = None):
        super(SecondForm, self).__init__(parent)
        
        self.edit = QLineEdit("")
        self.buttonW = QPushButton("Calculate the vowels and consonants")
        
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.buttonW)
        
        self.setLayout(layout)
        
        self.buttonW.clicked.connect(self.calculate_vowels_consonants)
        
    def calculate_vowels_consonants(self):
        text = self.edit.text()
        vowels = sum(1 for c in text if c.lower() in "aeiou")
        
        self.result_signal.emit(vowels)
        
        

class Form(QDialog):
    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        self.button = QPushButton("Open new window")
        self.label = QLabel("Text will appear here")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        self.button.clicked.connect(self.open_new_window)
        
    def open_new_window(self):
        self.w = SecondForm()
        
        self.w.result_signal.connect(self.update_label)
        self.w.show()
        
    def update_label(self, result):
        self.label.setText(f"Number of vowels: {result}")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())