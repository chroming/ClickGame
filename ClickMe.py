import sys
from PyQt4.QtGui import *
import random


def click_window():
    app = QApplication(sys.argv)
    desktop = QApplication.desktop().availableGeometry()
    win = QWidget()
    win.setWindowTitle("clickMe!")
    lb = QPushButton(win)
    lb.setText('Click!!!')
    win.setGeometry(desktop.width() / 2, desktop.height() / 2, 100, 100)
    lb.setGeometry(0, 0, 120, 100)

    def set_loc():
        #win.setGeometry(100, 100, 200, 100)
        #win.setGeometry(desktop.width()/2, desktop.height()/2, 100, 100)
        win.move(desktop.width()*random.randrange(0, 80)/100, desktop.height()*random.randrange(0, 80)/100)

    lb.clicked.connect(set_loc)

    win.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    click_window()