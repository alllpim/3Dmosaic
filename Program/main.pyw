import sys
import warnings

import matplotlib as mpl
from PySide6.QtWidgets import QApplication
from matplotlib import pyplot
from qt_material import apply_stylesheet

from MainWindow import MainWindow


def stylize() -> None:
    apply_stylesheet(app, theme="dark_yellow.xml")
    pyplot.style.use("dark_background")
    mpl.rcParams["axes.facecolor"] = "#31363B"
    mpl.rcParams["figure.facecolor"] = "#31363B"


if __name__ == "__main__":
    warnings.filterwarnings("ignore")

    app = QApplication(sys.argv)
    stylize()
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
