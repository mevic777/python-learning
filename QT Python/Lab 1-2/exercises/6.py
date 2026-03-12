import sys
from PySide6.QtWidgets import QDialog, QApplication, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QFont

class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent)

        self.label = QLabel("Pozitia mouse-ului")
        self.label_two = QLabel("In app or not in app")
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.label_two)
        self.setLayout(layout)

    
    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        
        self.label.setText(f"x: {x}, y: {y}")
    
        if self.underMouse(): self.label_two.setText("Inside the app")
        else: self.label_two.setText("Outside the app")
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())