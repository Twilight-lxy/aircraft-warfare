import multiprocessing
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from otherresource.Ranking_ui import Ui_MainWindow


class MyMainWindow(QMainWindow, QWidget, Ui_MainWindow):

    def __init__(self, queue: multiprocessing.Queue, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.queue = queue

    def closeEvent(self, event):
        self.queue.put(("close"))


def showRankingList(queue: multiprocessing.Queue):
    app = QApplication(sys.argv)
    RankList = MyMainWindow(queue)
    RankList.move(1200, 700)
    RankList.show()
    app.exec_()
