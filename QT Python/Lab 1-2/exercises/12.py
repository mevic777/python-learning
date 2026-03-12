import sys
from PySide6.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel, QPushButton, QLineEdit
import math


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.button = QPushButton("Calculate")
        self.edit = QLineEdit()
        self.label = QLabel("Results")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.button.clicked.connect(self.result_button)

    def result_button(self):
        r1 = self.last_digit()
        r2 = self.prim()
        r3 = self.cmmdc()

        self.label.setText(f"{r1}\n{r2}\nCel mai mare divizor prim: {r3}")

    def last_digit(self):
        m = int(self.edit.text())
        n = m % 10
        s = 0

        while m > 0:
            s += m % 10
            m //= 10

        return f"Ultima cifră: {n}, Suma cifrelor: {s}"

    def prim(self):
        m = int(self.edit.text())

        if m < 2:
            return "Nu este număr prim"

        for i in range(2, int(math.sqrt(m)) + 1):
            if m % i == 0:
                return "Nu este număr prim"

        return "Este număr prim"

    def cmmdc(self):
        m = int(self.edit.text())

        div = [i for i in range(2, m) if m % i == 0 and all(i % j for j in range(2, i))]

        return max(div) if div else "Nu există"


if __name__ == "__main__":
    app = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(app.exec())