# -*- coding: utf-8 -*-

'''
    ����顿
	PyQT5�����ڷ�����Ļ�м�
    
'''
import sys
from PyQt5.QtWidgets import QWidget, QToolTip , QApplication
from PyQt5.QtGui import QFont

class exp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('����һ��<b>������ʾ</b>')
        self.setGeometry(200, 300, 400, 400)
        self.setWindowTitle('������ʾdemo')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = exp()
    sys.exit(app.exec_())