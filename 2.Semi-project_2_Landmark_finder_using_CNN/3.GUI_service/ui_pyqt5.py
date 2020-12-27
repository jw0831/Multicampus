import resnet50
from resnet50 import testdir
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QGridLayout, QFileDialog, QLabel, QMainWindow, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap
import os
import shutil
from PyQt5.QtCore import Qt

class YEOGIYO(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self): # UI 실행 
        self.setGeometry(500,500,500,0)
        self.setWindowTitle("YEOGIYO!")
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is <b>Qwidget</b> a widget')
        self.num=0
        self.qclist=[]
        self.position=0
        self.Lgrid=QGridLayout()
        self.setLayout(self.Lgrid)
        self.label=QLabel('',self)

        self.label2 = QLabel('', self)
        self.label2.setAlignment(Qt.AlignCenter)
        self.font2 = self.label2.font()
        self.font2.setPointSize(15)
        self.font2.setBold(True)
        self.label2.setFont(self.font2)

        btn=QPushButton('이미지 불러오기', self)
        btn.setToolTip("This is a <b>QPushButton</b> a widget")
        btn.resize(btn.sizeHint())
        btn.move(200,50)

        self.Lgrid.addWidget(btn, 1, 1)
        self.Lgrid.addWidget(self.label, 2, 1)
        self.Lgrid.addWidget(self.label2, 3, 1)

        btn.clicked.connect(self.add_open)
        self.show()
        
    def add_open(self): # 파일 열기

        #이미지 폴더 삭제
        try:
            if os.path.exists('img'):
                shutil.rmtree('img')
        except OSError:
            print('Error: Creating directory. ' + 'a')

        FileOpen=QFileDialog.getOpenFileName(self, 'Open file', ',/')
        self.label.setText(FileOpen[0])

        path = "/".join(list(FileOpen[0].split("/"))[0:-1])
        fname = list(FileOpen[0].split("/"))[-1]

        #이미지 폴더 생성
        try:
            if not os.path.exists('img/img'):
                os.makedirs('img/img')
        except OSError:
            print('Error: Creating directory. ' + 'img')

        shutil.copyfile(os.path.join(path, fname),
                        os.path.join('img/img', fname))

        self.where = testdir(FileOpen[0])
        pixmap = QPixmap(FileOpen[0]).scaled(800, 500)
        self.label.setPixmap(pixmap)
        self.show()
        self.label2.setText("이곳은 \'" + self.where + "\' 입니다.")


        

if __name__=='__main__':
    app=QApplication(sys.argv)
    w=YEOGIYO()
    sys.exit(app.exec_())