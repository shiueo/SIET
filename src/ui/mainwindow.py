from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
)

from src.ui.ui_utils import fonts
from utils import global_path


class SIET_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Pretendard_SemiBold = QFont()
        fonts.load_font(w=self)

        self.setWindowTitle("SIET")
        self.resize(1280, 720)
        self.setWindowIcon(QIcon(global_path.get_proj_abs_path("assets/icon.png")))

        widget = QWidget()
        self.setCentralWidget(widget)

        self.GRID = QGridLayout(widget)

        self.FOOTER_BOX = QHBoxLayout()
        self.FOOTER_TEXT = QLabel(
            "© 2023-present <font color='#FF0A54'><u>shiüo</u></font>"
        )
        self.FOOTER_TEXT.setFont(QFont(self.Pretendard_Medium, 12))
        self.FOOTER_YOUTUBE = QPushButton()
        self.FOOTER_YOUTUBE.setIcon(QIcon(global_path.get_proj_abs_path("assets/icons/youtube.png")))
        self.FOOTER_GITHUB = QPushButton()
        self.FOOTER_GITHUB.setIcon(QIcon(global_path.get_proj_abs_path("assets/icons/github.png")))
        self.FOOTER_TWITTER = QPushButton()
        self.FOOTER_TWITTER.setIcon(QIcon(global_path.get_proj_abs_path("assets/icons/twitter.png")))
        self.FOOTER_SPOTIFY = QPushButton()
        self.FOOTER_SPOTIFY.setIcon(QIcon(global_path.get_proj_abs_path("assets/icons/spotify.png")))

        self.initUI()

    def initUI(self):
        with open(
            file=global_path.get_proj_abs_path("assets/stylesheet.txt"), mode="r"
        ) as f:
            self.setStyleSheet(f.read())

        self.FOOTER_BOX.addStretch()
        self.FOOTER_BOX.addWidget(self.FOOTER_TEXT)
        self.FOOTER_BOX.addWidget(self.FOOTER_GITHUB)
        self.FOOTER_BOX.addWidget(self.FOOTER_YOUTUBE)
        self.FOOTER_BOX.addWidget(self.FOOTER_SPOTIFY)
        self.FOOTER_BOX.addWidget(self.FOOTER_TWITTER)
        self.FOOTER_BOX.addStretch()

        self.GRID.addLayout(self.FOOTER_BOX, 0, 0, 1, 1)
