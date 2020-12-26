from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import ctypes
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QMessageBox, QWidget

from Functions import load
from Login_UI import Ui_LoginWindow


class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):
    signal = pyqtSignal()
    forget_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('校园一卡通管理系统登录')  # 设置窗口标题
        self.setWindowIcon(QIcon('logo.png'))  # 设置窗口图标
        # self.setStyleSheet('QWidget{background-color:%s}' % QColor(222, 222, 222).name())  # 设置窗口背景色
        self.setWindowOpacity(0.95)  # 设置整个计算器窗口的透明度
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  # 任务栏图标
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

        self.set_input()  # 输入账号和输入密码的设置

        # 将信号连接到对应槽函数
        self.login_button.clicked.connect(self.username_password)
        self.forget.clicked.connect(self.forget_password)
        self.login_close.clicked.connect(QCoreApplication.instance().quit)

    # 输入账号和输入密码的设置
    def set_input(self):
        self.input_username.setPlaceholderText("请输入账号")  # 灰色的占位符
        self.input_password.setPlaceholderText("请输入密码")  # 灰色的占位符
        self.input_username.setContextMenuPolicy(Qt.NoContextMenu)  # 禁止复制粘贴
        self.input_password.setContextMenuPolicy(Qt.NoContextMenu)  # 禁止复制粘贴
        self.input_password.setEchoMode(QLineEdit.Password)  # 输入时呈现圆点，不显示密码

    # 检查用户名与密码是否匹配
    def username_password(self):
        if load(self.input_username.text(), self.input_password.text()):
            self.hide()
            self.signal.emit()  # 发射信号
        else:
            QMessageBox.warning(self, "错误", "账号或密码错误！")
            self.input_password.setText('')
        pass

    # 忘记密码按钮触发的信号
    def forget_password(self):
        self.hide()
        self.forget_signal.emit()  # 发射忘记密码信号

    # 键盘登录
    def keyPressEvent(self, event):
        QWidget.keyPressEvent(self, event)
        key = event.key()
        if key == Qt.Key_Enter:
            self.username_password()
