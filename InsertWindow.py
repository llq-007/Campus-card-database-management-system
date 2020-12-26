from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import *
from Insert_UI import Ui_InsertWindow
from Functions import *


class InsertWindow(QMainWindow, Ui_InsertWindow):
    inserted_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('校园一卡通管理系统')  # 设置窗口标题
        self.setWindowIcon(QIcon('logo.png'))  # 设置窗口图标
        # self.setWindowIcon(QIcon('1.jpg'))  # 设置窗口图标
        # self.setStyleSheet('QWidget{background-color:%s}' % QColor(222, 222, 222).name())  # 设置窗口背景色
        self.setWindowOpacity(1)  # 设置整个计算器窗口的透明度
        # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  # 任务栏图标
        self.comboBox_sex.addItems([" ", "男", "女"])
        self.comboBox_college.addItems([" ", "计算机学院", "机械学院", "外国语学院"])
        self.comboBox_major.addItems([" ", "物联网工程", "计算机科学与技术", "软件工程", "通信工程", "信息安全"])
        # self.show()

        # 按钮绑定
        self.pushButton_insert.clicked.connect(self.insert)  # 插入事件
        self.comboBox_college.activated.connect(self.update_ComboBox)

    # 下拉框增加元素
    def update_ComboBox(self):
        coll = self.comboBox_college.currentText()
        self.comboBox_major.clear()
        if coll == "计算机学院":
            self.comboBox_major.addItems(["物联网工程", "计算机科学与技术", "软件工程", "通信工程", "信息安全"])
        elif coll == "机械学院":
            self.comboBox_major.addItems(["机械电子工程", "测控技术与仪器", "机械设计制造", "工业设计"])
        elif coll == "外国语学院":
            self.comboBox_major.addItems(["英语", "俄语", "日语", "法语", "西班牙语"])

    def insert(self):
        # 数据库交互
        id = self.lineEdit_id.text()
        name = self.lineEdit_name.text()
        sex = self.comboBox_sex.currentText()
        coll = self.comboBox_college.currentText()
        major = self.comboBox_major.currentText()
        number = self.lineEdit_phonenumber.text()
        Imformation(id, name, sex, coll, major, number)
        self.inserted_signal.emit()
        QMessageBox.information(self, "成功", "插入记录成功！")
        pass
