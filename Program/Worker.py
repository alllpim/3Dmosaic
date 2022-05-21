from typing import Callable

from PySide6.QtCore import QRunnable, Slot


class Worker(QRunnable):
    """
    Class for running functions in background threads
    """

    def __init__(self, func: Callable) -> None:
        """
        Class constructor

        """
        super().__init__()
        self.func = func

    @Slot()
    def run(self) -> None:
        """
        Method of starting the function

        """
        self.func()
