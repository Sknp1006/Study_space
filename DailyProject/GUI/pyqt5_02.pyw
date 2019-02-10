#!/usr/bin/python3
#  -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)  #初始显示的大小
    w.move(1400, 300)   #初始显示的位置
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())