# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cards.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Cards(object):
    def setupUi(self, Cards):
        if not Cards.objectName():
            Cards.setObjectName(u"Cards")
        Cards.resize(800, 600)
        self.centralwidget = QWidget(Cards)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 130, 801, 471))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pbtn01 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img = QButtonGroup(Cards)
        self.pbtn_img.setObjectName(u"pbtn_img")
        self.pbtn_img.addButton(self.pbtn01)
        self.pbtn01.setObjectName(u"pbtn01")
        font = QFont()
        font.setFamily(u"Adobe Gothic Std B")
        self.pbtn01.setFont(font)

        self.gridLayout.addWidget(self.pbtn01, 0, 0, 1, 1)

        self.pbtn09 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn09)
        self.pbtn09.setObjectName(u"pbtn09")
        self.pbtn09.setFont(font)

        self.gridLayout.addWidget(self.pbtn09, 3, 0, 1, 1)

        self.pbtn07 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn07)
        self.pbtn07.setObjectName(u"pbtn07")
        self.pbtn07.setFont(font)

        self.gridLayout.addWidget(self.pbtn07, 2, 2, 1, 1)

        self.pbtn06 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn06)
        self.pbtn06.setObjectName(u"pbtn06")
        self.pbtn06.setFont(font)

        self.gridLayout.addWidget(self.pbtn06, 2, 1, 1, 1)

        self.pbtn05 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn05)
        self.pbtn05.setObjectName(u"pbtn05")
        self.pbtn05.setFont(font)

        self.gridLayout.addWidget(self.pbtn05, 2, 0, 1, 1)

        self.pbtn02 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn02)
        self.pbtn02.setObjectName(u"pbtn02")
        self.pbtn02.setFont(font)

        self.gridLayout.addWidget(self.pbtn02, 0, 1, 1, 1)

        self.pbtn03 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn03)
        self.pbtn03.setObjectName(u"pbtn03")
        self.pbtn03.setFont(font)

        self.gridLayout.addWidget(self.pbtn03, 0, 2, 1, 1)

        self.pbtn04 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn04)
        self.pbtn04.setObjectName(u"pbtn04")
        self.pbtn04.setFont(font)

        self.gridLayout.addWidget(self.pbtn04, 0, 3, 1, 1)

        self.pbtn10 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn10)
        self.pbtn10.setObjectName(u"pbtn10")
        self.pbtn10.setFont(font)

        self.gridLayout.addWidget(self.pbtn10, 3, 1, 1, 1)

        self.pbtn11 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn11)
        self.pbtn11.setObjectName(u"pbtn11")
        self.pbtn11.setFont(font)

        self.gridLayout.addWidget(self.pbtn11, 3, 2, 1, 1)

        self.pbtn08 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn08)
        self.pbtn08.setObjectName(u"pbtn08")
        self.pbtn08.setFont(font)

        self.gridLayout.addWidget(self.pbtn08, 2, 3, 1, 1)

        self.pbtn12 = QPushButton(self.gridLayoutWidget)
        self.pbtn_img.addButton(self.pbtn12)
        self.pbtn12.setObjectName(u"pbtn12")
        self.pbtn12.setFont(font)

        self.gridLayout.addWidget(self.pbtn12, 3, 3, 1, 1)

        self.lcd_time = QLCDNumber(self.centralwidget)
        self.lcd_time.setObjectName(u"lcd_time")
        self.lcd_time.setGeometry(QRect(310, 30, 201, 81))
        Cards.setCentralWidget(self.centralwidget)

        self.retranslateUi(Cards)

        QMetaObject.connectSlotsByName(Cards)
    # setupUi

    def retranslateUi(self, Cards):
        Cards.setWindowTitle(QCoreApplication.translate("Cards", u"\u8bb0\u5fc6\u7ffb\u76d8", None))
        self.pbtn01.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn09.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn07.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn06.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn05.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn02.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn03.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn04.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn10.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn11.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn08.setText(QCoreApplication.translate("Cards", u"PushButton", None))
        self.pbtn12.setText(QCoreApplication.translate("Cards", u"PushButton", None))
    # retranslateUi

