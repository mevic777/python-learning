import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):

    def __init__(self):
        super().__init__()

        self.timelabel = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(750, 400, 300, 100)

        vbox = QVBoxLayout()

        vbox.addWidget(self.timelabel)
        self.setLayout(vbox)

        self.timelabel.setAlignment(Qt.AlignCenter)
        self.timelabel.setStyleSheet("font-size: 150px;"
                                     "color: #26ff00;")

        font_id = QFontDatabase.addApplicationFont("font.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.timelabel.setFont(my_font)

        self.setStyleSheet("background: black;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.timelabel.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()

    clock.show()
    sys.exit(app.exec_())  # it starts the main loop of the application
    # handles events of key presses or mouse clicks
