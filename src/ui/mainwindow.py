from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
    QMenu,
)

from utils import global_path


class SIET_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set the window title
        self.setWindowTitle("SIET")
        # Set the initial window size
        self.resize(1280, 720)
        # Set the window icon using the QIcon class and the path to the icon file
        self.setWindowIcon(QIcon(global_path.get_proj_abs_path("assets/icon.png")))

        # Create a QWidget instance to serve as the central widget
        widget = QWidget()
        # Set the central widget of the main window
        self.setCentralWidget(widget)

        # Initialize the user interface
        self.initUI()

    def initUI(self):
        # Open and read the contents of the stylesheet file
        with open(
            file=global_path.get_proj_abs_path("assets/stylesheet.txt"), mode="r"
        ) as f:
            # Set the stylesheet for the main window using the read contents
            self.setStyleSheet(f.read())
