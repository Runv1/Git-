import sqlite3
import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.setGeometry(500, 250, 1000, 1000)
        self.setWindowTitle('Рисование')
        self.pushButton = QPushButton('Рисовать', self)
        self.pushButton.move(10, 10)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        try:
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            qp.setBrush(QColor(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
            # Рисуем прямоугольник заданной кистью
            qp.drawEllipse(random.randrange(50, 850), random.randrange(50, 850), 100, 100)
            # Завершаем рисование
            qp.end()
        except Exception as e:
            print(e)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
