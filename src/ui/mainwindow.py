import pathlib
import webbrowser

from PySide6.QtGui import QIcon, QFont, QDragEnterEvent, QDropEvent
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


def FOOTER_BTN_GITHUB():
    webbrowser.open("https://github.com/shiueo/SIET/")


def FOOTER_BTN_YOUTUBE():
    webbrowser.open("https://www.youtube.com/@shiueo")


class SIET_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Pretendard_Medium = QFont()
        self.Pretendard_SemiBold = QFont()
        fonts.load_font(w=self)

        self.setWindowTitle("SIET")
        self.resize(1280, 720)
        self.setAcceptDrops(True)
        self.setWindowIcon(QIcon(global_path.get_proj_abs_path("assets/icon.png")))
        self.statusBar().setFont(QFont(self.Pretendard_Medium, 10))
        self.statusBar().showMessage("Ready")

        # VARIABLES
        self.target_image_path = None

        widget = QWidget()
        self.setCentralWidget(widget)

        self.GRID = QGridLayout(widget)

        self.FOOTER_BOX = QHBoxLayout()
        self.FOOTER_TEXT = QLabel(
            "© 2023-present <font color='#FF0A54'><u>shiüo</u></font>"
        )
        self.FOOTER_TEXT.setFont(QFont(self.Pretendard_Medium, 12))
        self.FOOTER_YOUTUBE = QPushButton()
        self.FOOTER_YOUTUBE.setIcon(
            QIcon(global_path.get_proj_abs_path("assets/icons/youtube.png"))
        )
        self.FOOTER_YOUTUBE.clicked.connect(lambda: FOOTER_BTN_YOUTUBE())
        self.FOOTER_GITHUB = QPushButton()
        self.FOOTER_GITHUB.setIcon(
            QIcon(global_path.get_proj_abs_path("assets/icons/github.png"))
        )
        self.FOOTER_GITHUB.clicked.connect(lambda: FOOTER_BTN_GITHUB())
        self.FOOTER_TWITTER = QPushButton()
        self.FOOTER_TWITTER.setIcon(
            QIcon(global_path.get_proj_abs_path("assets/icons/twitter.png"))
        )
        self.FOOTER_SPOTIFY = QPushButton()
        self.FOOTER_SPOTIFY.setIcon(
            QIcon(global_path.get_proj_abs_path("assets/icons/spotify.png"))
        )
        self.FOOTER_DISCORD = QPushButton()
        self.FOOTER_DISCORD.setIcon(
            QIcon(global_path.get_proj_abs_path("assets/icons/discord.png"))
        )

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
        self.FOOTER_BOX.addWidget(self.FOOTER_DISCORD)
        self.FOOTER_BOX.addWidget(self.FOOTER_SPOTIFY)
        self.FOOTER_BOX.addWidget(self.FOOTER_TWITTER)
        self.FOOTER_BOX.addStretch()

        self.GRID.addLayout(self.FOOTER_BOX, 0, 0, 1, 1)

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        tmp = [i.toLocalFile() for i in event.mimeData().urls()][0]
        if pathlib.Path(tmp).suffix in [".png", ".jpg"]:
            self.target_image_path = tmp
            self.statusBar().showMessage(
                f"{pathlib.Path(self.target_image_path).name} loaded."
            )
        else:
            self.statusBar().showMessage(
                f"Require image files in formats like PNG, JPEG, JPG, ... . :: {pathlib.Path(tmp).name}"
            )
