import sys
from PySide6.QtWidgets import QDialog, QApplication, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PySide6.QtGui import QFont

class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        
        self.label = QLabel("Mouse coordinates will appear here.")
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        self.setMouseTracking(True)
    
    def mouseMoveEvent(self, event):
        x, y = event.position().x(), event.position().y()
        
        self.label.setText(f"Coordinates: x({x}), y({y})")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())