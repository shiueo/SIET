import os

global ABS_PATH


def set_proj_abs_path(path: str):
    global ABS_PATH
    ABS_PATH = os.path.dirname(path)


def get_proj_abs_path(path: str):
    return os.path.join(ABS_PATH, path)
