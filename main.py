import sys
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(589, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 402, 111, 61))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Кнопка"))


class Example(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.qp = QPainter()
        self.initUI()
        self.flag = ''
        self.x = 300
        self.y = 200
        self.colors = ['yellow', 'red', 'blue', 'green']
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def initUI(self):
        self.setWindowTitle('Draw')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(qp)
        qp.end()

    def drawText(self, qp):
        color = random.choice(self.colors)
        qp.setBrush(QColor(color))
        r = random.randint(1, 300)
        qp.drawEllipse(self.x - r // 2, self.y - r // 2, r, r)


# sys._excepthook = sys.excepthook
#
#
# def my_exception_hook(exctype, value, traceback):
#     print(exctype, value, traceback)
#     sys._excepthook(exctype, value, traceback)
#     sys.exit(1)
#
#
# sys.excepthook = my_exception_hook


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Example()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
