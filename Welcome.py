# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WELCOME.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SuperHero import Hero
import pickle
from Fight import Ui_MainWindow

with open('heroes.pickle', 'rb') as heroes:
    all_heroes = pickle.load(heroes)

#hero_list = (hero.hero_stats() for hero in all_heroes)
hero_cnt = len(all_heroes)

class Ui_WelcomeWindow(object):

    def __init__(self, WelcomeWindow):
        self.WelcomeWindow = WelcomeWindow


    def setupUi(self, WelcomeWindow):
        WelcomeWindow.setObjectName("WelcomeWindow")
        WelcomeWindow.resize(800, 600)
        WelcomeWindow.setFixedSize(800, 600)

        WelcomeWindow.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.centralwidget = QtWidgets.QWidget(WelcomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBoxpl1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxpl1.setGeometry(QtCore.QRect(130, 330, 541, 41))
        self.comboBoxpl1.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.comboBoxpl1.setObjectName("comboBoxpl1")
        for hero in all_heroes.values():
            self.comboBoxpl1.addItem(hero.hero_stats())
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 390, 200, 30))
        self.pushButton.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.pushButton.setObjectName("pushButton")
        self.comboBoxpl2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxpl2.setGeometry(QtCore.QRect(130, 480, 541, 41))
        self.comboBoxpl2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.comboBoxpl2.setObjectName("comboBoxpl2")
        for hero in all_heroes.values():
            self.comboBoxpl2.addItem(hero.hero_stats())
        self.BtnStart = QtWidgets.QPushButton(self.centralwidget)
        self.BtnStart.setGeometry(QtCore.QRect(350, 540, 95, 28))
        self.BtnStart.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.BtnStart.setObjectName("BtnStart")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 440, 131, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_2.setGeometry(QtCore.QRect(130, 290, 131, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(215, 0, 370, 320))
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.comboBoxpl1.raise_()
        self.pushButton.raise_()
        self.comboBoxpl2.raise_()
        self.BtnStart.raise_()
        self.label.raise_()
        self.label_2.raise_()
        WelcomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WelcomeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        WelcomeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WelcomeWindow)
        self.statusbar.setObjectName("statusbar")
        WelcomeWindow.setStatusBar(self.statusbar)


        self.retranslateUi(WelcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(WelcomeWindow)



    def retranslateUi(self, WelcomeWindow):
        _translate = QtCore.QCoreApplication.translate
        WelcomeWindow.setWindowTitle(_translate("WelcomeWindow", "MainWindow"))
        # self.comboBoxpl1.setItemText(0, _translate("WelcomeWindow", "Hero 1"))
        self.pushButton.setText(_translate("WelcomeWindow", "PLAY AGAINST THE COMPUTER"))
        # self.comboBoxpl2.setItemText(0, _translate("WelcomeWindow", "Hero 1"))
        self.BtnStart.setText(_translate("WelcomeWindow", "START"))
        self.label.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">Choose Player 2</span></p></body></html>"))
        self.label_2.setText(_translate("WelcomeWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#000000;\">Choose Player 1</span></p></body></html>"))
        self.label_3.setText(_translate("WelcomeWindow", "<html><head/><body><p><img src=\"kapow.jpg\"/></p></body></html>"))

        self.BtnStart.clicked.connect(self.start_2p)
        self.pushButton.clicked.connect(self.start_comp)

    def start_2p(self):
        hero_id1 = int(self.comboBoxpl1.currentText().split(".")[0])
        hero_id2 = int(self.comboBoxpl2.currentText().split(".")[0])

        hero_c = all_heroes[hero_id1]
        hero_h = all_heroes[hero_id2]

        with open('image_c.jpg', 'wb') as img:
            img.write(hero_c.image)

        with open('image_h.jpg', 'wb') as img:
            img.write(hero_h.image)

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(hero_c, hero_h, 2, self.window)
        self.ui.setupUi(self.window)
        WelcomeWindow.hide()
        self.window.show()

    def start_comp(self):
        hero_id = int(self.comboBoxpl1.currentText().split(".")[0])


        hero_h = all_heroes[hero_id]

        hero_c = Hero.random_hero(all_heroes)

        with open('image_c.jpg', 'wb') as img:
            img.write(hero_c.image)

        with open('image_h.jpg', 'wb') as img:
            img.write(hero_h.image)

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(hero_c, hero_h, 1, self.window)
        self.ui.setupUi(self.window)
        WelcomeWindow.hide()
        self.window.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WelcomeWindow = QtWidgets.QMainWindow()

    ui = Ui_WelcomeWindow(WelcomeWindow)
    ui.setupUi(WelcomeWindow)
    WelcomeWindow.show()
    sys.exit(app.exec_())



