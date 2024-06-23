import sys
import PyQt5.QtWidgets 
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QButtonGroup
from src.classes.GameRecord import GameRecord
from otherresource.Ranking_ui import Ui_MainWindow





class MyMainWindow(QMainWindow,QWidget,Ui_MainWindow): 
        
        def __init__(self,parent =None):
            super(MyMainWindow,self).__init__(parent)
            self.setupUi(self)
#if __name__ == "__main__":
def showRankingList():
    app = QApplication(sys.argv)
    RankList = MyMainWindow()
    

    RankList.move(1200,700)
    RankList.show()
    app.exec_()


# rankingList=getRankingListfromDB()

# rankingList=[a,b,c,d,..... ]
# a = GameRecord
# a.getUsername(