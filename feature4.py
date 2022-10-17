# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feature4.ui'
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


class Ui_window_feature4(object):
    def setupUi(self, window_feature4):
        window_feature4.setObjectName("window_feature4")
        window_feature4.resize(510, 600)
        self.label_tip = QtWidgets.QLabel(window_feature4)
        self.label_tip.setGeometry(QtCore.QRect(50, 210, 261, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_tip.setFont(font)
        self.label_tip.setObjectName("label_tip")
        self.label_tip_2 = QtWidgets.QLabel(window_feature4)
        self.label_tip_2.setGeometry(QtCore.QRect(10, 290, 361, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_tip_2.setFont(font)
        self.label_tip_2.setObjectName("label_tip_2")
        self.label_title = QtWidgets.QLabel(window_feature4)
        self.label_title.setGeometry(QtCore.QRect(90, 120, 330, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_create = QtWidgets.QPushButton(window_feature4)
        self.pushButton_create.setGeometry(QtCore.QRect(205, 400, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.pushButton_create.setFont(font)
        self.pushButton_create.setObjectName("pushButton_create")
        self.label_title_2 = QtWidgets.QLabel(window_feature4)
        self.label_title_2.setGeometry(QtCore.QRect(150, 160, 210, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_2.setFont(font)
        self.label_title_2.setObjectName("label_title_2")
        self.lineEdit_codenum = QtWidgets.QLineEdit(window_feature4)
        self.lineEdit_codenum.setGeometry(QtCore.QRect(330, 230, 120, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_codenum.setFont(font)
        self.lineEdit_codenum.setObjectName("lineEdit_codenum")
        self.lineEdit_codenum.setValidator(QtGui.QIntValidator())
        self.lineEdit_codenum_2 = QtWidgets.QLineEdit(window_feature4)
        self.lineEdit_codenum_2.setGeometry(QtCore.QRect(370, 290, 120, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit_codenum_2.setFont(font)
        self.lineEdit_codenum_2.setObjectName("lineEdit_codenum_2")
        self.label_tip_4 = QtWidgets.QLabel(window_feature4)
        self.label_tip_4.setGeometry(QtCore.QRect(50, 240, 251, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_tip_4.setFont(font)
        self.label_tip_4.setObjectName("label_tip_4")

        # 生成
        self.pushButton_create.clicked.connect(lambda: self.create())

        self.retranslateUi(window_feature4)
        QtCore.QMetaObject.connectSlotsByName(window_feature4)

    def retranslateUi(self, window_feature4):
        _translate = QtCore.QCoreApplication.translate
        window_feature4.setWindowTitle(_translate("window_feature4", "Form"))
        self.label_tip.setText(_translate("window_feature4", "请输入需要生产的带数据"))
        self.label_tip_2.setText(_translate("window_feature4", "请输入数据分析编号（3位字母）："))
        self.label_title.setText(_translate("window_feature4", "含数据分析功能的防伪编码"))
        self.pushButton_create.setText(_translate("window_feature4", "生成"))
        self.label_title_2.setText(_translate("window_feature4", "（5A62M0583D2）"))
        self.label_tip_4.setText(_translate("window_feature4", "分析功能的防伪码数量："))

    def create(self):
        # 获取所需生成的数量
        scode_count_num = self.lineEdit_codenum.text()
        scode_analysis_num = self.lineEdit_codenum_2.text()
        if len(scode_count_num) == 0 or len(scode_analysis_num) == 0:
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "警告", "请填写所需的所有信息！", QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)
        elif int(scode_count_num) == 0:
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "警告", "产品数量错误！", QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)
        elif len(scode_analysis_num) != 3:
            QtWidgets.QMessageBox.warning(QtWidgets.QWidget(), "警告", "数据分析编号错误，请输入三位字母组成的数据分析编号！",
                                          QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)
        else:
            # 判断是否存在防伪码保存的文件夹，如果没有则生成
            if not os.path.exists("codepath"):
                os.mkdir("codepath")
            # 将分析码全部转换为大写
            scode_analysis_num_upper = scode_analysis_num[0].upper() \
                                       + scode_analysis_num[1].upper() \
                                       + scode_analysis_num[2].upper()
            # 生成防伪码
            scodestr = []
            for i in range(int(scode_count_num)):
                # 产生随机插入分析编号的位置
                insert_address = sorted(random.sample("0123456789", 3))
                for i in range(3):
                    insert_address[i] = int(insert_address[i])
                temp = ''
                for j in range(9):
                    temp = temp + chr(random.randrange(ord('0'), ord('9') + 1))
                temp = temp[0:insert_address[0]] + scode_analysis_num_upper[0] \
                       + temp[insert_address[0]:insert_address[1]] + scode_analysis_num_upper[1] \
                       + temp[insert_address[1]:insert_address[2]] + scode_analysis_num_upper[2] \
                       + temp[insert_address[2]:]
                sql = 'SELECT * FROM fangweima4 WHERE code='+'\''+temp+'\''
                check = query(sql,None)
                if check: #检查后可以添加 数据库加入  新生成的文件中加入
                    sql = 'INSERT INTO fangweima4 VALUES(%s);'
                    insert(sql,temp)
                    scodestr.append(temp)
            # 打开文件并写入防伪码
            with open("codepath/" + scode_analysis_num_upper + "scode-feature4.txt", 'w') as f:
                for item in scodestr:
                    f.write(item + '\n')
            # 提示用户生成成功
            tip_sentence = "已生成含数据分析功能的防伪码共计：" \
                           + str(scode_count_num) \
                           + "\n防伪码文件位于“codepath/" + scode_analysis_num_upper + "scode-feature4.txt”文件下\n请及时备份以防文件被覆盖\n"
            QtWidgets.QMessageBox.information(QtWidgets.QWidget(), "提示", tip_sentence, QtWidgets.QMessageBox.Yes,
                                              QtWidgets.QMessageBox.Yes)
