import random

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import *
from Main_UI import Ui_MainWindow
from Functions import *


# 在PyQt5里创建的是MainWindow，不是Widget，需要注意的是，创建的元素一定要调用正确。
class MainWindow(QMainWindow, Ui_MainWindow):
    insert_signal = pyqtSignal()
    batch_signal = pyqtSignal()
    query_flag = 0
    check_list = []
    delete_f = -1
    delete_t = -1

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('校园一卡通管理系统')  # 设置窗口标题
        self.setWindowIcon(QIcon('logo.png'))  # 设置窗口图标
        # self.setStyleSheet('QWidget{background-color:%s}' % QColor(222, 222, 222).name())  # 设置窗口背景色
        self.setWindowOpacity(1)  # 设置整个计算器窗口的透明度
        # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  # 任务栏图标
        self.lineEdit_id.setText("")
        self.lineEdit_name.setText("")
        self.lineEdit_phonenumber.setText("")
        self.comboBox_sex.addItems(["", "男", "女"])
        self.comboBox_college.addItems(["", "计算机学院", "机械学院", "外国语学院"])
        self.comboBox_major.addItems(["", "物联网工程", "计算机科学与技术", "软件工程", "通信工程", "信息安全"])
        self.comboBox_sex_2.addItems(["", "充值", "饮食", "电费", "水费", "车费"])
        self.query_flag = 0
        self.check_list = []
        self.delete_f = -1
        self.delete_t = -1

        # 信号和槽函数绑定
        # 栏目1（学生基本信息）
        self.pushButton_query.clicked.connect(self.query)  # 为按钮添加点击事件
        self.comboBox_college.activated.connect(self.update_ComboBox)
        self.pushButton_insert.clicked.connect(self.insert_button_signal)  # 弹出插入窗口
        self.pushButton_delete.clicked.connect(self.deleteConfirm)  # 删除操作
        self.tableWidget.itemChanged.connect(self.update_tableWidget)  # 查找操作
        self.tableWidget.cellPressed.connect(self.update_flag)  # 更新查找标记
        self.tableWidget.itemSelectionChanged.connect(self.update_selected) # 更新选择区域
        self.pushButton_batch.clicked.connect(self.batch_button_signal)
        # 栏目2（交易记录）
        self.pushButton_query_2.clicked.connect(self.upadate_tableWidget2)  # 查记录
        # 栏目3（充值界面按钮绑定）
        self.top_up_button.clicked.connect(self.top_up)

    # 更新选择区域
    def update_selected(self):
        list = self.tableWidget.selectedRanges()
        for temp in list:
            # print(temp.topRow(), temp.bottomRow())
            self.delete_f = temp.topRow()
            self.delete_t = temp.bottomRow()

    # 更新交易记录
    def upadate_tableWidget2(self):
        id2 = self.lineEdit_id_2.text()
        name2 = self.lineEdit_name_2.text()
        type2 = self.comboBox_sex_2.currentText()
        result = TransactionRecords(id2, name2, type2)

        # 调用数据库
        lable1 = ['学号', '姓名', '消费类型', '消费时间', '金额变动', '余额']
        self.tableWidget_2.setRowCount(result.__len__())
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setHorizontalHeaderLabels(lable1)
        self.tableWidget_2.setColumnWidth(0, 200)
        self.tableWidget_2.setColumnWidth(1, 150)
        self.tableWidget_2.setColumnWidth(2, 100)
        self.tableWidget_2.setColumnWidth(3, 300)
        self.tableWidget_2.setColumnWidth(4, 138)
        self.tableWidget_2.setColumnWidth(5, 138)
        for i in range(0, self.tableWidget_2.rowCount()):
            self.tableWidget_2.setRowHeight(i, 45)

        for i in range(result.__len__()):
            temp = result[i]
            for j in range(0, lable1.__len__()):
                if temp[j] is not None:
                    if j == 4:
                        money = str(temp[j])
                        if money[0] != '-':
                            money = "+ " + money
                        else:
                            money = "- " + money[1:]
                        self.tableWidget_2.setItem(i, 4, QTableWidgetItem(money))
                    else:
                        self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(temp[j])))
                else:
                    self.tableWidget_2.setItem(i, j, QTableWidgetItem(" "))


    # 修改表信息
    def update_tableWidget(self):
        # print(self.tableWidget.selectedItems()==None)
        # print("x: " + str(self.tableWidget.selectedIndexes()[0].row()) + ",  y: " + str(self.tableWidget.selectedIndexes()[0].column()))
        # print("请求修改信息")
        if self.query_flag == 1:
            return
        i = self.tableWidget.currentIndex().row()
        j = self.tableWidget.currentIndex().column()
        lable = ['学号', '姓名', '性别', '学院', '专业', '手机号', '余额']
        # print(self.tableWidget.item(i,0).text(),lable[j],self.tableWidget.item(i,j).text())
        DataUpdate(self.tableWidget.item(i, 0).text(), lable[j], self.tableWidget.item(i, j).text())

        # print("修改信息成功")
        # print(str(self.tableWidget.currentIndex().row()))
        # print(self.tableWidget.rowCount())

    # 更新标志
    def update_flag(self):
        # print("flag")
        self.query_flag = 0

    # 批量插入按钮发射信号
    def batch_button_signal(self):
        self.batch_signal.emit()  # 发射信号

    # 插入按钮发射信号
    def insert_button_signal(self):
        self.insert_signal.emit()  # 发射信号

    # 批量删除
    def delete2(self):
        if self.delete_f == -1 and self.delete_t == -1:
            # QMessageBox.warning(self, "失败", "请框选需要删除的记录！")
            return False
        for i in range(self.delete_f,self.delete_t + 1):
            DeleteData(str(self.tableWidget.item(i, 0).text()))
        self.query()
        QMessageBox.information(self, "信息", "删除记录成功！")
        self.delete_t = -1
        self.delete_f = -1
        return True

    # 确认删除
    def deleteConfirm(self):
        message_box = QMessageBox()
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        message_box.setWindowTitle("提示")
        message_box.setText("确认删除？")
        message_box.setWindowIcon(QIcon('logo.png'))
        yes = message_box.button(QMessageBox.Yes)
        yes.clicked.connect(self.delete)  # 点击此按钮则退出程序
        message_box.exec()

    # 删除按钮发射信号
    def delete(self):
        if self.delete2():
            return
        flag = 0
        for i in range(0, self.tableWidget.rowCount()):
            if self.check_list[i].checkState() == 2:
                flag = 1
                DeleteData(str(self.tableWidget.item(i, 0).text()))
        if flag == 1:
            self.query()
            QMessageBox.information(self, "提示", "删除记录成功！")
            self.delete_t = -1
            self.delete_f = -1
        else:
            QMessageBox.critical(self, "失败", "请勾选需要删除的记录！")

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

    def query(self):
        self.query_flag = 1
        id = self.lineEdit_id.text()
        name = self.lineEdit_name.text()
        sex = self.comboBox_sex.currentText()
        coll = self.comboBox_college.currentText()
        major = self.comboBox_major.currentText()
        number = self.lineEdit_phonenumber.text()
        result = informationInput(id, name, sex, coll, major, number)

        self.check_list.clear()
        for i in range(0, result.__len__()):
            # 下面六行用于生成居中的checkbox，不知道有没有别的好方法
            ck = QCheckBox()
            self.check_list.append(ck)

        # 调用数据库
        self.tableWidget.setRowCount(result.__len__())
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(['学号', '姓名', '性别', '学院', '专业', '手机号', '余额', '选择'])
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 50)
        self.tableWidget.setColumnWidth(3, 160)
        self.tableWidget.setColumnWidth(4, 160)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setColumnWidth(6, 120)
        self.tableWidget.setColumnWidth(7, 87)
        for i in range(0, self.tableWidget.rowCount()):
            self.tableWidget.setRowHeight(i, 44)

        lable1 = ['学号', '姓名', '性别', '学院', '专业', '手机号', '余额', '选择']
        for i in range(result.__len__()):
            temp = result[i]
            for j in range(0, lable1.__len__()):
                if j < 7:
                    if temp[lable1[j]] is not None:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(temp[lable1[j]])))
                    else:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(" "))
                else:
                    h = QHBoxLayout()
                    h.setAlignment(Qt.AlignCenter)
                    h.addWidget(self.check_list[i])
                    w = QWidget()
                    w.setLayout(h)
                    self.tableWidget.setCellWidget(i, j, w)

    def top_up(self):
        username = self.top_up_id.text()
        money = self.top_up_money.text()
        result = Recharge(money, username)
        if result == 0:
            QMessageBox.warning(self, "错误", "请输入有效学号！")
            self.top_up_id.setText('')
        elif result == 1:
            QMessageBox.warning(self, "错误", "请输入正确金额！")
            self.top_up_money.setText('')
        else:
            QMessageBox.information(self, "成功", "充值成功！")
            self.top_up_id.setText('')
            self.top_up_money.setText('')
