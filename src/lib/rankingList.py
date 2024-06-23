import multiprocessing
import os
import sys
import PyQt5.QtCore
import PyQt5.QtWidgets 
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QButtonGroup
from src.classes.GameRecord import GameRecord
from otherresource.Ranking_ui import Ui_MainWindow





class MyMainWindow(QMainWindow,QWidget,Ui_MainWindow): 
        
        def __init__(self,queue:multiprocessing.Queue,parent =None):
            super(MyMainWindow,self).__init__(parent)
            self.setupUi(self)
            self.queue = queue
        def closeEvent(self, event):
            self.queue.put(("close"))
#if __name__ == "__main__":
def showRankingList(queue:multiprocessing.Queue):
    app = QApplication(sys.argv)
    RankList = MyMainWindow(queue)
    RankList.move(1200,700)
    RankList.show()
    app.exec_()


# rankingList=getRankingListfromDB()

# rankingList=[a,b,c,d,..... ]
# a = GameRecord
# a.getUsername(