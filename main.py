import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPainter, QColor
import random
from PyQt5 import uic


class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.initUI()
        self.flag = ''
        self.x = 300
        self.y = 200
        self.colors = ['black', 'cyan', 'darkCyan', 'red', 'darkRed',
                       'magenta', 'darkMagenta', 'green', 'darkGreen', 'yellow', 'darkYellow']
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def initUI(self):
        self.setWindowTitle('Draw text')
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
