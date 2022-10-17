# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feature3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os
import random
import pymysql
def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test1')
    return conn

def insert(sql, args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    cur.close()
    conn.close()
def query(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql,args)
    results = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if results: #已存在 不可添加数据
        return False
    else:#未存在，可以添加数据
        return True

class Ui_window_feature3(object):
    def setupUi(self, window_feature3):
        window_feature3.setObjectName("window_feature3")
        window_feature3.resize(508, 600)
        self.label_title_2 = QtWidgets.QLabel(window_feature3)
        self.label_title_2.setGeometry(QtCore.QRect(25, 210, 460, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_2.setFont(font)
        self.label_title_2.setObjectName("label_title_2")
        self.label_title = QtWidgets.QLabel(window_feature3)
        self.label_title.setGeometry(QtCore.QRect(130, 170, 250, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_create = QtWidgets.QPushButton(window_feature3)
        self.pushButton_create.setGeometry(QtCore.QRect(205, 340, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.lineEdit_codenum = QtWidgets.QLineEdit(window_feature3)
        self.lineEdit_codenum.setGeometry(QtCore.QRect(370, 260, 120, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_codenum.setFont(font)
        self.lineEdit_codenum.setObjectName("lineEdit_codenum")
        self.lineEdit_codenum.setValidator(QtGui.QIntValidator())
        self.label_tip = QtWidgets.QLabel(window_feature3)
        self.label_tip.setGeometry(QtCore.QRect(20, 260, 340, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_tip.setFont(font)
        self.label_tip.setObjectName("label_tip")

        # 生成
        self.pushButton_create.clicked.connect((lambda: self.create()))

        self.retranslateUi(window_feature3)
        QtCore.QMetaObject.connectSlotsByName(window_feature3)

    def retranslateUi(self, window_feature3):
        _translate = QtCore.QCoreApplication.translate
        window_feature3.setWindowTitle(_translate("window_feature3", "Form"))
        self.label_title_2.setText(_translate("window_feature3", "（7A734-CATI45-7BJ1WW-LFF4E3-EPWARU型）"))
        self.label_title.setText(_translate("window_feature3", "29位混合产品序列号"))
        self.pushButton_create.setText(_translate("window_feature3", "生成"))
        self.label_tip.setText(_translate("window_feature3", "请输入您需要生成的防伪码数量:"))

    def create(self):
        # 获取所需生成的数量
        scode_count_num = self.lineEdit_codenum.text()
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        if int(scode_count_num) == 0:
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "警告", "产品数量错误！", QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)
        else:
            # 判断是否存在防伪码保存的文件夹，如果没有则生成
            if not os.path.exists("codepath"):
                os.mkdir("codepath")
            # 生成防伪码
            scodestr = []
            for j in range(int(scode_count_num)):
                temp = ''
                for i in range(1, 30):
                    if i % 6 == 0:
                        temp = temp + '-'
                    temp = temp + random.choice(letters)
                sql = 'SELECT * FROM fangweima3 WHERE code='+'\''+temp+'\''
                check = query(sql,None)
                if check: #检查后可以添加 数据库加入  新生成的文件中加入
                    sql = 'INSERT INTO fangweima3 VALUES(%s);'
                    insert(sql,temp)
                    scodestr.append(temp)
            # 打开文件并写入防伪码
            with open("codepath/scode-feature3.txt", 'w') as f:
                for item in scodestr:
                    f.write(item + '\n')
            # 提示用户生成成功
            tip_sentence = "已生成29位防伪码共计：" \
                           + str(scode_count_num) \
                           + "\n防伪码文件位于“codepath/scode-feature3.txt”文件下\n请及时备份以防文件被覆盖\n"
            QtWidgets.QMessageBox.information(QtWidgets.QWidget(), "提示", tip_sentence, QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)

