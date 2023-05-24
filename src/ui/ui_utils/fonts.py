from PySide6.QtGui import QFontDatabase

from utils import global_path


def load(path):
    return QFontDatabase.applicationFontFamilies(
        QFontDatabase.addApplicationFont(global_path.get_proj_abs_path(path))
    )[0]


def load_font(w):
    w.Pretendard_Black = load("assets/fonts/Pretendard-Black.otf")
    w.Pretendard_Bold = load("assets/fonts/Pretendard-Bold.otf")
    w.Pretendard_ExtraBold = load("assets/fonts/Pretendard-ExtraBold.otf")
    w.Pretendard_ExtraLight = load("assets/fonts/Pretendard-ExtraLight.otf")
    w.Pretendard_Light = load("assets/fonts/Pretendard-Light.otf")
    w.Pretendard_Medium = load("assets/fonts/Pretendard-Medium.otf")
    w.Pretendard_Regular = load("assets/fonts/Pretendard-Regular.otf")
    w.Pretendard_SemiBold = load("assets/fonts/Pretendard-SemiBold.otf")
    w.Pretendard_Thin = load("assets/fonts/Pretendard-Thin.otf")
