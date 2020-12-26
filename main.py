# Campus-card-database-management-systemfrom PyQt5.QtWidgets import QApplication

from BatchInsertedWindow import BatchInsertedWindow
from ForgetWindow import ResetWindow, SecurityQuestionWindow
from LoginWindow import LoginWindow
from MainWindow import MainWindow
from InsertWindow import InsertWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_widget = LoginWindow()  # 窗口控件
    login_widget.show()

    main_widget = MainWindow()  # 窗口控件
    forget_widget = SecurityQuestionWindow()  # 密保窗口
    reset_widget = ResetWindow()  # 重置密码窗口
    insert_widget = InsertWindow()  # 窗口控件
    batch_insert_widget = BatchInsertedWindow()  # 批量插入窗口

    login_widget.signal.connect(main_widget.show)  # 连接槽函数
    login_widget.forget_signal.connect(forget_widget.show)  # 显示忘记密码窗口
    forget_widget.signal.connect(reset_widget.show)  # 显示重置密码窗口
    forget_widget.back_signal.connect(login_widget.show)  # 显示登录窗口
    reset_widget.signal.connect(login_widget.show)  # 回到登录窗口
    reset_widget.back_signal.connect(login_widget.show)  # 回到登录窗口
    main_widget.batch_signal.connect(batch_insert_widget.show)  # 显示批量插入窗口

    main_widget.insert_signal.connect(insert_widget.show)  # 连接槽函数
    insert_widget.inserted_signal.connect(main_widget.query)  # 更新数据

    sys.exit(app.exec_())

