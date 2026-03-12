import sys
import PySide6.QtGui
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        
        self.label_one = QLabel(f"Width: {self.size().width()}, Height: {self.size().height()}")
        self.label_two = QLabel("Starea butonului stang")
        
        layout = QVBoxLayout()
        layout.addWidget(self.label_one)
        layout.addWidget(self.label_two)

        self.setLayout(layout)
        self.resize(400, 300)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label_two.setText("Button pressed")
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label_two.setText("Button released")
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())