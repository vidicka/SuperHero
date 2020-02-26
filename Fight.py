# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FIGHT.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SuperHero import Hero_fight
from Winner import Ui_WinnerWindow
import time
from PyQt5.QtCore import  pyqtSignal

class Ui_MainWindow(object):



    def __init__(self, hero_c, hero_h, MainWindow):
        self.hero_h = hero_h.hero_to_fight()
        self.hero_c = hero_c.hero_to_fight()
        self.MainWindow = MainWindow
        self.trigger = pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1095, 794)
        MainWindow.setStyleSheet("background-color: rgb(0,0,0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_comp = QtWidgets.QLabel(self.centralwidget)
        self.image_comp.setGeometry(QtCore.QRect(250, 100, 161, 251))
        self.image_comp.setObjectName("image_comp")
        self.image_human = QtWidgets.QLabel(self.centralwidget)
        self.image_human.setEnabled(True)
        self.image_human.setGeometry(QtCore.QRect(690, 100, 161, 251))
        self.image_human.setObjectName("image_human")
        self.health_comp = QtWidgets.QLabel(self.centralwidget)
        self.health_comp.setGeometry(QtCore.QRect(220, 80, self.hero_c.health, 16))
        self.health_comp.setStyleSheet("color: rgb(255, 0, 4);\n"
"background-color: rgb(255, 0, 4);\n"
"background-color: rgb(212, 0, 3);")
        self.health_comp.setObjectName("health_comp")
        self.health_human = QtWidgets.QLabel(self.centralwidget)
        self.health_human.setGeometry(QtCore.QRect(660, 80, self.hero_h.health, 16))
        self.health_human.setStyleSheet("color: rgb(255, 0, 4);\n"
"background-color: rgb(255, 0, 4);\n"
"background-color: rgb(212, 0, 3);")
        self.health_human.setObjectName("health_human")
        self.Melleebtn = QtWidgets.QPushButton(self.centralwidget)
        self.Melleebtn.setGeometry(QtCore.QRect(690, 400, 93, 28))
        self.Melleebtn.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Melleebtn.setObjectName("Melleebtn")
        self.Rangebtn = QtWidgets.QPushButton(self.centralwidget)
        self.Rangebtn.setGeometry(QtCore.QRect(690, 450, 93, 28))
        self.Rangebtn.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Rangebtn.setObjectName("Rangebtn")
        self.Rangebtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Rangebtn_2.setGeometry(QtCore.QRect(690, 530, 93, 28))
        self.Rangebtn_2.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Rangebtn_2.setObjectName("Rangebtn_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(810, 400, 161, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(810, 450, 161, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(810, 500, 271, 101))
        self.label_3.setObjectName("label_3")
        self.label_stats_human = QtWidgets.QLabel(self.centralwidget)
        self.label_stats_human.setGeometry(QtCore.QRect(870, 110, 111, 211))
        self.label_stats_human.setObjectName("label_stats_human")
        self.label_stats_comp = QtWidgets.QLabel(self.centralwidget)
        self.label_stats_comp.setGeometry(QtCore.QRect(120, 110, 111, 211))
        self.label_stats_comp.setObjectName("label_stats_comp")
        self.label_damage = QtWidgets.QLabel(self.centralwidget)
        self.label_damage.setGeometry(QtCore.QRect(480, 200, 161, 31))
        self.label_damage.setObjectName("label_damage")
        self.label_attack_log = QtWidgets.QLabel(self.centralwidget)
        self.label_attack_log.setGeometry(QtCore.QRect(110, 390, 371, 201))
        self.label_attack_log.setObjectName("label_attack_log")
        self.label_damage_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_damage_2.setGeometry(QtCore.QRect(480, 150, 161, 31))
        self.label_damage_2.setObjectName("label_damage_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 26))
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
        self.image_comp.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"image_c.jpg\"/></p></body></html>"))
        self.image_human.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"image_h.jpg\"/></p></body></html>"))
        self.health_comp.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#f8e801;\">{self.hero_c.name}</span></p></body></html>"))
        self.health_human.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; color:#f8e801;\">{self.hero_h.name}</span></p></body></html>"))
        self.Melleebtn.setText(_translate("MainWindow", "Melee Atack"))
        self.Rangebtn.setText(_translate("MainWindow", "Ranged Attack"))
        self.Rangebtn_2.setText(_translate("MainWindow", "Power Attack"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#f8e801;\">Uses STR and CMB</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#f8e801;\">Uses SPD and CMB</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#f8e801;\">Uses larger from INT and PWR and</span></p><p><span style=\" font-size:9pt; color:#f8e801;\"> larger from STR and SPD, </span></p><p><span style=\" font-size:9pt; color:#f8e801;\">needs 3 round to charge</span></p></body></html>"))
        human_stat_str = f"<html><head/><body><p><span style=\" font-size:9pt; color:#f8e801;\">STR: {self.hero_h.strength}</span></p><p><span style=\" font-size:9pt; color:#f8e801;\">SPD: {self.hero_h.speed}</span></p><p><span style=\" font-size:9pt; color:#f8e801;\">CMB: {self.hero_h.combat}</span></p><p><span style=\" font-size:9pt; color:#f8e801;\">POW: {self.hero_h.power}</span></p><p><span style=\" font-size:9pt; color:#f8e801;\">INT: {self.hero_h.intelligence}</span></p></body></html>"
        self.label_stats_human.setText(_translate("MainWindow", human_stat_str))
        comp_stat_str = f"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; color:#f8e801;\">STR: {self.hero_c.strength}</span></p><p align=\"right\"><span style=\" font-size:9pt; color:#f8e801;\">SPD: {self.hero_c.speed}</span></p><p align=\"right\"><span style=\" font-size:9pt; color:#f8e801;\">CMB: {self.hero_c.combat}</span></p><p align=\"right\"><span style=\" font-size:9pt; color:#f8e801;\">POW: {self.hero_c.power}</span></p><p align=\"right\"><span style=\" font-size:9pt; color:#f8e801;\">INT: {self.hero_c.intelligence}</span></p></body></html>"
        self.label_stats_comp.setText(_translate("MainWindow", comp_stat_str))
        self.label_damage.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#f8e801;\">DAMAGE DELT: 0</span></p></body></html>"))
        self.label_attack_log.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#f8e801;\">Attack 1: Comp delt 0 dmg</span></p></body></html>"))
        self.label_damage_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#f8e801;\">MELEE ATACK</span></p></body></html>"))

        self.Melleebtn.clicked.connect(self.melee)
        # self.Melleebtn.clicked.connect(self.com_fight)

        # self.Melleebtn.released.connect(self.com_fight)
        self.Rangebtn.clicked.connect(self.ranged)
        # self.Rangebtn.released.connect(self.com_fight)
        self.Rangebtn_2.clicked.connect(self.power_up)
        # self.Rangebtn_2.released.connect(self.com_fight)



    def melee(self):
        self.fight(self.hero_h, self.hero_c, 'melee')

        self.fight(self.hero_c, self.hero_h, self.hero_c.choose_attack())

    def ranged(self):
        self.fight(self.hero_h, self.hero_c, 'ranged')
    
        self.fight(self.hero_c, self.hero_h, self.hero_c.choose_attack())

    def power_up(self):
        if self.hero_h.round_cnt % 3 != 0:
            return
        self.fight(self.hero_h, self.hero_c, 'power_up')

        self.fight(self.hero_c, self.hero_h, self.hero_c.choose_attack())
    

    def com_fight(self):
        self.fight(self.hero_c, self.hero_h, self.hero_c.choose_attack())

    def fight(self, hero, other, attack_type):

        print(hero.health)
        print(other.health)
        if attack_type == 'power_up':
            if hero.round_cnt % 3 != 0:

                return
            else:
                hero.power_up_hero()
                hero.round_cnt += 1
                # hero.round_cnt = 0
                return

        other.take_dmg(hero.attack(attack_type))


        hero.round_cnt += 1



    
        if other.health <= 0:

            with open('image_w.jpg', 'wb') as img:
                img.write(hero.image)


            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_WinnerWindow(hero)
            self.ui.setupUi(self.window)
            self.MainWindow.hide()

            self.window.show()
      
        # self.setupUi(self.MainWindow)
        self.health_comp.setGeometry(QtCore.QRect(220, 80, self.hero_c.health, 16))
        self.health_human.setGeometry(QtCore.QRect(660, 80, self.hero_h.health, 16))

        print(hero.health)
        print(other.health)
        print(hero.round_cnt)


# import image_c_rc
# import image_h_rc

if __name__ == "__main__":
    import sys
    import pickle
    from random import randint
    from SuperHero import Hero 
    import os

    try:
        with open('heros.pickle', 'rb') as heroes:
            all_heroes = pickle.load(heroes)
    except FileNotFoundError:
        command = 'SuperHero.py'
        os.system(command)
        with open('heros.pickle', 'rb') as heroes:
            all_heroes = pickle.load(heroes)
    
    hero_c = Hero.random_hero(all_heroes).hero_to_fight()

    hero_h = Hero.random_hero(all_heroes).hero_to_fight()

    with open('image_c.jpg', 'wb') as img:
        img.write(hero_c.image)

    with open('image_h.jpg', 'wb') as img:
        img.write(hero_h.image)


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(hero_c, hero_h, MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

