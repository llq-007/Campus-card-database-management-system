# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(664, 505)
        LoginWindow.setMinimumSize(QtCore.QSize(664, 505))
        LoginWindow.setMaximumSize(QtCore.QSize(664, 505))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -2, 671, 261))
        self.background.setStyleSheet("image: url(:/background/background.png);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(150, 430, 381, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton{color: rgb(255, 255, 255); background-color: #1dc5fc; border-radius:8px}\n"
"\n"
"QPushButton:hover{Background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #23cdfc, stop:1 #1cd7fc);}\n"
"\n"
"QPushButton:pressed{Background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 #1cd7fc, stop:1 #23cdfc);}\n"
"")
        self.login_button.setObjectName("login_button")
        self.input_username = QtWidgets.QLineEdit(self.centralwidget)
        self.input_username.setGeometry(QtCore.QRect(200, 290, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_username.setFont(font)
        self.input_username.setStyleSheet("QLineEdit{border:0.5px solid gray; border-radius:8px}\n"
"")
        self.input_username.setText("")
        self.input_username.setObjectName("input_username")
        self.input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_password.setGeometry(QtCore.QRect(200, 360, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("QLineEdit{border:0.5px solid gray; border-radius:8px}")
        self.input_password.setText("")
        self.input_password.setObjectName("input_password")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(120, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(120, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.forget = QtWidgets.QPushButton(self.centralwidget)
        self.forget.setGeometry(QtCore.QRect(560, 460, 101, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.forget.setFont(font)
        self.forget.setStyleSheet("QPushButton:hover{Background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));}\n"
"\n"
"QPushButton:pressed{border: 0px;}")
        self.forget.setFlat(True)
        self.forget.setObjectName("forget")
        self.login_close = QtWidgets.QPushButton(self.centralwidget)
        self.login_close.setGeometry(QtCore.QRect(610, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login_close.setFont(font)
        self.login_close.setStyleSheet("QPushButton{color: rgb(255, 255, 255); border-radius:10px}\n"
"\n"
"QPushButton:hover{Background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));}\n"
"\n"
"QPushButton:pressed{Background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));}")
        self.login_close.setObjectName("login_close")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "self"))
        self.login_button.setText(_translate("LoginWindow", "登录"))
        self.password.setText(_translate("LoginWindow", "密码："))
        self.username.setText(_translate("LoginWindow", "账号："))
        self.forget.setText(_translate("LoginWindow", "忘记密码"))
        self.login_close.setText(_translate("LoginWindow", "×"))
import background_rc
