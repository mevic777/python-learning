import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class Form(QDialog):

    def __init__(self, parent = None):
        super(Form, self).__init__(parent)
        
        self.label_one = QLabel("Text 1")
        self.label_two = QLabel("Text 2")
        self.label_two.setStyleSheet("color: red;")

        layout = QVBoxLayout()
        layout.addWidget(self.label_one)
        layout.addWidget(self.label_two)

        self.setLayout(layout)
        
        self.resize(500, 400)

    def mouseMoveEvent(self, event):
        cursor = event.pos()
        
        label_one_pos = self.label_one.pos()
        label_two_pos = self.label_two.pos()
        
        dis_one = cursor - label_one_pos
        dis_two = cursor - label_two_pos
        
        dis_one = dis_one.manhattanLength()
        dis_two = dis_two.manhattanLength()
        
        if dis_one < dis_two:
            self.label_one.setStyleSheet("color: red;")
            self.label_two.setStyleSheet("color: white;")
        else:
            self.label_one.setStyleSheet("color: white;")
            self.label_two.setStyleSheet("color: red;")
    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    form = Form()
    form.show()

    sys.exit(app.exec())