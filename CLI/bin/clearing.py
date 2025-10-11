import shutil
import os

def _clear_pyc():
    folder_paths = [
                    "./CLI/bin/__pycache__",
                    "./CLI/lib/__pycache__",
                    "./CLI/__pycache__"
            ]
    for folder in folder_paths:
        if os.path.exists(folder):
            shutil.rmtree(folder)

