import sys
import os
import random
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_cards import Ui_Cards


class MyCards(QMainWindow, Ui_Cards):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_button()
        self.init_img()
        self.show()
        self.clicked_num = 0
        self.match_img = {
            1: {
                'pbtn': None,
                'pbtn_img': None
            },
            2: {
                'pbtn': None,
                'pbtn_img': None
            }
        }
        self.first_clicked = True
        self.time = 0
        self.right_count = 0
        self.pbtn_img.buttonClicked.connect(self.pbtn_func)

    def init_button(self):
        pbtn_list = self.pbtn_img.buttons()
        for pbtn in pbtn_list:
            pbtn.setText('')
            pbtn.setIcon(QIcon('bg.png'))
            pbtn.setIconSize(QSize(150, 150))
            pbtn.setCheckable(True)

    def init_img(self):
        images_type = ['.png', '.jpg', '.bmp', '.jpeg']
        files = os.listdir('images')
        all_imgs = []
        for file in files:
            ext = os.path.splitext(file)[-1]
            if ext in images_type:
                all_imgs.append('images' + os.sep + file)

        random_imgs = random.sample(all_imgs, 6)
        grid_imgs = random_imgs + random_imgs
        random.shuffle(grid_imgs)
        pbtn_list = self.pbtn_img.buttons()
        self.grids = dict(zip(pbtn_list, grid_imgs))

    def pbtn_func(self):
        if self.first_clicked:
            self.first_clicked = False
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)
        if self.clicked_num < 2:
            QApplication.processEvents()
            pbtn = self.pbtn_img.checkedButton()
            if pbtn != self.match_img[1]['pbtn'] and pbtn in self.pbtn_img.buttons():
                self.clicked_num += 1
                pbtn.setIcon(QIcon(self.grids[pbtn]))
                self.match_img[self.clicked_num]['pbtn'] = pbtn
                self.match_img[self.clicked_num]['pbtn_img'] = self.grids[pbtn]
                timer = QTimer()
                timer.singleShot(500, self.judge)

    def judge(self):
        if self.clicked_num == 2:
            self.clicked_num = 0
            if self.match_img[1]['pbtn_img'] != self.match_img[2]['pbtn_img']:
                self.match_img[1]['pbtn'].setIcon(QIcon('bg.png'))
                self.match_img[2]['pbtn'].setIcon(QIcon('bg.png'))
            else:
                self.pbtn_img.removeButton(self.match_img[1]['pbtn'])
                self.pbtn_img.removeButton(self.match_img[2]['pbtn'])
                self.right_count += 1
                if self.right_count == 6:
                    self.timer.stop()
            self.match_img[1]['pbtn'] = self.match_img[2]['pbtn'] = None

    def update_time(self):
        self.time += 1
        self.lcd_time.display(self.time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyCards()
    sys.exit(app.exec_())
