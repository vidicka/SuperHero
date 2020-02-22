# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WELCOME.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SuperHero import Hero
import pickle
from random import randint
from Fight import Ui_MainWindow

with open('heros.pickle', 'rb') as heroes:
    all_heroes = pickle.load(heroes)

#hero_list = (hero.hero_stats() for hero in all_heroes)
hero_cnt = len(all_heroes)

class Ui_WelcomeWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(120, 0, 0);\n"
"background-color: rgb(43, 0, 68);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 70, 371, 101))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 190, 371, 101))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 330, 761, 41))
        self.comboBox.setStyleSheet("color: rgb(245, 217, 0);\n"
"font: 9pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
#        self.comboBox.addItem("")
        for hero in all_heroes:
            self.comboBox.addItem(hero.hero_stats())
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 420, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#f8e801;\">WELCOME</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#f8e801;\">CHOOSE YOUR HERO</span></p></body></html>"))
        # self.comboBox.setItemText(0, _translate("MainWindow", "Hero 1"))
        # self.comboBox.setItemText(1, _translate("MainWindow", "Hero 2"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton.clicked.connect(self.start_click)

    def start_click(self):
        hero_id = self.comboBox.currentText().split(".")[0]

        rand = randint(1,hero_cnt)

        hero_h = all_heroes[int(hero_id)-1]

        hero_c = all_heroes[rand-1]

        with open('image_c.jpg', 'wb') as img:
            img.write(hero_c.image)

        with open('image_h.jpg', 'wb') as img:
            img.write(hero_h.image)

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(hero_c, hero_h)
        self.ui.setupUi(self.window)
        self.window.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_WelcomeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

