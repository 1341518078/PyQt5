# -*- coding: utf-8 -*- 
'''
    ����顿
	����PyQt5��Qwidget���ʹ���ֲᵽ����
  
    ���ߣ���ƽ
    
'''

import sys
from PyQt5.QtWidgets import QWidget

out = sys.stdout
sys.stdout = open(r'E:\QWidget.txt' , 'w')
help( QTableWidget )
sys.stdout.close()
sys.stdout = out