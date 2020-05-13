"""
Author: John Jamora
Date Created: 10/05/2020
This program automatically moves files between directories, based on their file type.
"""

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
import sys


class FileMover(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    """
    Initializes the GUI window
    """
    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("This is a <b>QWidget</b> widget")

        btn = QPushButton('Button', self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(500, 100, 1000, 800)
        self.setWindowTitle("File Mover")
        self.setWindowIcon(QIcon("arrow.png"))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fm = FileMover()
    sys.exit(app.exec_())  # Ensures a smooth exit
