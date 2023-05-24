from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
    QMenu, QHBoxLayout, QLabel,
)

from src.ui.ui_utils import fonts
from utils import global_path


class SIET_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Pretendard_SemiBold = QFont()
        fonts.load_font(w=self)
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

        self.GRID = QGridLayout(widget)

        self.FOOTER_BOX = QHBoxLayout()
        self.FOOTER_TEXT = QLabel("© 2023-present <font color='#FF0A54'><u>shiüo</u></font>")
        self.FOOTER_TEXT.setFont(QFont(self.Pretendard_SemiBold, 12))

        # Initialize the user interface
        self.initUI()

    def initUI(self):
        # Open and read the contents of the stylesheet file
        with open(
            file=global_path.get_proj_abs_path("assets/stylesheet.txt"), mode="r"
        ) as f:
            # Set the stylesheet for the main window using the read contents
            self.setStyleSheet(f.read())

        self.FOOTER_BOX.addStretch()
        self.FOOTER_BOX.addWidget(self.FOOTER_TEXT)
        self.FOOTER_BOX.addStretch()

        self.GRID.addLayout(self.FOOTER_BOX, 0, 0, 1, 1)

