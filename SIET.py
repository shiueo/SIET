import os
import sys

from PySide6.QtWidgets import QApplication

from src.ui.mainwindow import SIET_MainWindow

from utils import global_path

global_path.set_proj_abs_path(os.path.abspath(__file__))

SIET_QApplication = QApplication()
SIET_Window = SIET_MainWindow()
SIET_Window.show()
sys.exit(SIET_QApplication.exec())
