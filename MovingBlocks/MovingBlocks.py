from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QMessageBox, QSplitter
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QDesktopWidget,  QMainWindow, QDialog
import sys, random
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, pyqtSlot, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import *
import winsound         # for sound  

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        hbox = QHBoxLayout(self)

        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

 
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
       

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
