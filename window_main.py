# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import ui_rc
from PyQt5 import QtCore, QtGui, QtWidgets

from feature1 import Ui_window_feature1
from feature2 import Ui_window_feature2
from feature3 import Ui_window_feature3
from feature4 import Ui_window_feature4
from feature5 import Ui_window_feature5
from feature6 import Ui_window_feature6
from feature7 import Ui_window_feature7
from feature8 import Ui_window_feature8
from feature9 import Ui_window_feature9

class Ui_window_main(object):
    def setupUi(self, window_main):
        window_main.setObjectName("window_main")
        window_main.resize(510, 600)
        window_main.setMinimumSize(QtCore.QSize(510, 600))
        window_main.setMaximumSize(QtCore.QSize(510, 600))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("./res/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.centralwidget = QtWidgets.QWidget(window_main)
        self.centralwidget.setObjectName("centralwidget")
        self.label_segement = QtWidgets.QLabel(self.centralwidget)
        self.label_segement.setGeometry(QtCore.QRect(0, 300, 980, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_segement.setFont(font)
        self.label_segement.setObjectName("label_segement")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(80, 220, 350, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_segement_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_segement_2.setGeometry(QtCore.QRect(0, 200, 980, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_segement_2.setFont(font)
        self.label_segement_2.setObjectName("label_segement_2")
        window_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.action_accode = QtWidgets.QMenu(self.menubar)
        self.action_accode.setObjectName("action_accode")
        self.action_feature7 = QtWidgets.QAction(self.menubar)
        self.action_feature7.setObjectName("action_feature7")
        self.action_feature8 = QtWidgets.QAction(self.menubar)
        self.action_feature8.setObjectName("action_feature8")
        self.action_feature9 = QtWidgets.QAction(self.menubar)
        self.action_feature9.setObjectName("action_feature9")
        self.action_exit = QtWidgets.QAction(self.menubar)
        self.action_exit.setObjectName("action_exit")
        window_main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window_main)
        self.statusbar.setObjectName("statusbar")
        window_main.setStatusBar(self.statusbar)
        self.action_feature1 = QtWidgets.QAction(window_main)
        self.action_feature1.setObjectName("action_feature1")
        self.action_feature2 = QtWidgets.QAction(window_main)
        self.action_feature2.setObjectName("action_feature2")
        self.action_feature3 = QtWidgets.QAction(window_main)
        self.action_feature3.setObjectName("action_feature3")
        self.action_feature4 = QtWidgets.QAction(window_main)
        self.action_feature4.setObjectName("action_feature4")
        self.action_feature5 = QtWidgets.QAction(window_main)
        self.action_feature5.setObjectName("action_feature5")
        self.action_feature6 = QtWidgets.QAction(window_main)
        self.action_feature6.setObjectName("action_feature6")
        self.action_accode.addAction(self.action_feature1)
        self.action_accode.addAction(self.action_feature2)
        self.action_accode.addAction(self.action_feature3)
        self.action_accode.addAction(self.action_feature4)
        self.action_accode.addAction(self.action_feature5)
        self.action_accode.addAction(self.action_feature6)
        self.menubar.addAction(self.action_accode.menuAction())
        self.menubar.addAction(self.action_feature7)
        self.menubar.addAction(self.action_feature8)
        self.menubar.addAction(self.action_feature9)
        self.menubar.addAction(self.action_exit)

        # go feature1
        self.action_feature1.triggered.connect(lambda: self.go_feature1(window_main))
        # go feature2
        self.action_feature2.triggered.connect(lambda: self.go_feature2(window_main))
        # go feature3
        self.action_feature3.triggered.connect(lambda: self.go_feature3(window_main))
        # go feature4
        self.action_feature4.triggered.connect(lambda: self.go_feature4(window_main))
        # go feature5
        self.action_feature5.triggered.connect(lambda: self.go_feature5(window_main))
        # go feature6
        self.action_feature6.triggered.connect(lambda: self.go_feature6(window_main))
        # go feature7
        self.action_feature7.triggered.connect(lambda: self.go_feature7(window_main))
        # go feature8
        self.action_feature8.triggered.connect(lambda: self.go_feature8(window_main))
        # go feature9
        self.action_feature9.triggered.connect(lambda: self.go_feature9(window_main))
        # 退出
        self.action_exit.triggered.connect(window_main.close)

        self.retranslateUi(window_main)
        QtCore.QMetaObject.connectSlotsByName(window_main)

    def retranslateUi(self, window_main):
        _translate = QtCore.QCoreApplication.translate
        window_main.setWindowTitle(_translate("window_main", "security code sys"))
        window_main.setWindowIcon(self.icon)
        self.label_segement.setText(_translate("window_main", "******************************************"))
        self.label_title.setText(_translate("window_main", "security code sys"))
        self.label_segement_2.setText(_translate("window_main", "******************************************"))
        self.action_accode.setTitle(_translate("window_main", "Access code"))
        self.action_feature7.setText(_translate("window_main", "bar code"))
        self.action_feature8.setText(_translate("window_main", "QR code"))
        self.action_feature9.setText(_translate("window_main", "防伪码抽奖"))
        self.action_exit.setText(_translate("window_main", "exit"))
        self.action_feature1.setText(_translate("window_main", "6 digit"))
        self.action_feature2.setText(_translate("window_main", "9 digit"))
        self.action_feature3.setText(_translate("window_main", "29 digit mix"))
        self.action_feature4.setText(_translate("window_main", "含数据分析功能"))
        self.action_feature5.setText(_translate("window_main", "batch generate"))
        self.action_feature6.setText(_translate("window_main", "supplement"))

    def go_feature1(self, window_main):
        window_feature1 = Ui_window_feature1()
        Maintain = QtWidgets.QMainWindow()
        window_feature1.setupUi(Maintain)
        window_main.setCentralWidget(Maintain)

    def go_feature2(self, window_main):
        window_feature2 = Ui_window_feature2()
        Maintain = QtWidgets.QMainWindow()
        window_feature2.setupUi(Maintain)
        window_main.setCentralWidget(Maintain)

    def go_feature3(self, window_main):
        window_feature3 = Ui_window_feature3()
        Maintain = QtWidgets.QMainWindow()
        window_feature3.setupUi(Maintain)
        window_main.setCentralWidget(Maintain)

    def go_feature4(self, window_main):
        window_feature4 = Ui_window_feature4()
        Maintain = QtWidgets.QMainWindow()
        window_feature4.setupUi(Maintain)
        window_main.setCentralWidget(Maintain)

    def go_feature5(self, window_main):
        window_feature5 = Ui_window_feature5()
        Maintain = QtWidgets.QMainWindow()
        window_feature5.setupUi(Maintain)
        window_main.setCentralWidget(Maintain)

    def go_feature6(self, window_main):
        window_feature6 = Ui_window_feature6()
        Maintain = QtWidgets.QMainWindow()
        window_feature6.setupUi(Maintain)
        window_main.setCentralWidget(Maintain)

    def go_feature7(self, window_main):
        window_feature7 = Ui_window_feature7()
        Maintain = QtWidgets.QMainWindow()
        window_feature7.setupUi(Maintain)
        window_main.setCentralWidget(Maintain)

    def go_feature8(self, window_main):
        window_feature8 = Ui_window_feature8()
        Maintain = QtWidgets.QMainWindow()
        window_feature8.setupUi(Maintain)
        window_main.setCentralWidget(Maintain)

    def go_feature9(self, window_main):
        window_feature9 = Ui_window_feature9()
        Maintain = QtWidgets.QMainWindow()
        window_feature9.setupUi(Maintain)
        window_main.setCentralWidget(Maintain)
