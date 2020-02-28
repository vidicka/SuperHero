# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FIGHT_2p.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SuperHero import Hero_fight
from Winner import Ui_WinnerWindow

class Ui_MainWindow(object):

    def __init__(self, hero_c, hero_h, players, MainWindow):
        self.hero_h = hero_h.hero_to_fight()
        self.hero_c = hero_c.hero_to_fight()
        self.players = players
        self.MainWindow = MainWindow
        self.damage_msg = ''
        self.attack_msg = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1095, 765)
        MainWindow.setFixedSize(1095, 765)
        MainWindow.setStyleSheet("background-color: rgb(43, 0, 68);\n"
"background-color: rgb(229, 229, 229);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_comp = QtWidgets.QLabel(self.centralwidget)
        self.image_comp.setGeometry(QtCore.QRect(244, 100, 161, 251))
        self.image_comp.setObjectName("image_comp")
        self.image_human = QtWidgets.QLabel(self.centralwidget)
        self.image_human.setEnabled(True)
        self.image_human.setGeometry(QtCore.QRect(690, 100, 161, 251))
        self.image_human.setObjectName("image_human")
        self.border_health_comp = QtWidgets.QLabel(self.centralwidget)
        self.border_health_comp.setGeometry(QtCore.QRect(224, 79, 202, 16))
        self.border_health_comp.setStyleSheet("color: rgb(0, 0, 4);\n"
"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(240,240, 240);")
        self.border_health_comp.setFrameShape(QtWidgets.QFrame.Box)
        self.border_health_comp.setText("")
        self.border_health_comp.setObjectName("border_health_comp")
        self.healt_human = QtWidgets.QLabel(self.centralwidget)
        self.healt_human.setGeometry(QtCore.QRect(671, 81, self.hero_h.health, 14))
        self.healt_human.setToolTipDuration(1)
        self.healt_human.setStyleSheet("color: rgb(255, 0, 4);\n"
"background-color: rgb(255, 0, 4);\n"
"background-color: rgb(212, 0, 3);")
        self.healt_human.setText("")
        self.healt_human.setObjectName("healt_human")
        self.Mellee_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Mellee_btn.setGeometry(QtCore.QRect(690, 400, 95, 28))
        self.Mellee_btn.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Mellee_btn.setObjectName("Mellee_btn")
        self.Range_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Range_btn.setGeometry(QtCore.QRect(690, 450, 95, 28))
        self.Range_btn.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Range_btn.setObjectName("Range_btn")
        self.Power_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Power_btn.setGeometry(QtCore.QRect(690, 510, 95, 28))
        self.Power_btn.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Power_btn.setObjectName("Power_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(810, 400, 161, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(810, 450, 161, 31))
        self.label_2.setObjectName("label_2")
        self.label_stats_human = QtWidgets.QLabel(self.centralwidget)
        self.label_stats_human.setGeometry(QtCore.QRect(870, 110, 111, 211))
        self.label_stats_human.setObjectName("label_stats_human")
        self.label_stats_comp = QtWidgets.QLabel(self.centralwidget)
        self.label_stats_comp.setGeometry(QtCore.QRect(114, 110, 111, 211))
        self.label_stats_comp.setObjectName("label_stats_comp")
        self.label_damage = QtWidgets.QLabel(self.centralwidget)
        self.label_damage.setGeometry(QtCore.QRect(490, 200, 161, 31))
        self.label_damage.setObjectName("label_damage")
        self.label_attack_type = QtWidgets.QLabel(self.centralwidget)
        self.label_attack_type.setGeometry(QtCore.QRect(490, 150, 135, 31))
        self.label_attack_type.setObjectName("label_attack_type")
        self.comp_name = QtWidgets.QLabel(self.centralwidget)
        self.comp_name.setGeometry(QtCore.QRect(244, 40, 161, 31))
        self.comp_name.setObjectName("comp_name")
        self.human_name = QtWidgets.QLabel(self.centralwidget)
        self.human_name.setGeometry(QtCore.QRect(690, 40, 161, 31))
        self.human_name.setObjectName("human_name")
        self.border_health_human = QtWidgets.QLabel(self.centralwidget)
        self.border_health_human.setGeometry(QtCore.QRect(670, 80, 202, 16))
        self.border_health_human.setStyleSheet("color: rgb(0, 0, 4);\n"
"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(240,240, 240);")
        self.border_health_human.setFrameShape(QtWidgets.QFrame.Box)
        self.border_health_human.setText("")
        self.border_health_human.setObjectName("border_health_human")
        self.health_comp = QtWidgets.QLabel(self.centralwidget)
        self.health_comp.setGeometry(QtCore.QRect(225, 80, self.hero_c.health, 14))
        self.health_comp.setToolTipDuration(1)
        self.health_comp.setStyleSheet("color: rgb(255, 0, 4);\n"
"background-color: rgb(255, 0, 4);\n"
"background-color: rgb(212, 0, 3);")
        self.health_comp.setText("")
        self.health_comp.setObjectName("health_comp")
        self.Tact_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Tact_btn.setGeometry(QtCore.QRect(690, 560, 95, 28))
        self.Tact_btn.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Tact_btn.setObjectName("Tact_btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(810, 560, 261, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(810, 510, 261, 41))
        self.label_5.setObjectName("label_5")
        self.Range_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Range_btn_2.setGeometry(QtCore.QRect(310, 450, 95, 28))
        self.Range_btn_2.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Range_btn_2.setObjectName("Range_btn_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 510, 261, 41))
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 400, 151, 31))
        self.label_3.setObjectName("label_3")
        self.Mellee_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Mellee_btn_2.setGeometry(QtCore.QRect(310, 400, 95, 28))
        self.Mellee_btn_2.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Mellee_btn_2.setObjectName("Mellee_btn_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 450, 241, 31))
        self.label_7.setObjectName("label_7")
        self.Tact_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Tact_btn_2.setGeometry(QtCore.QRect(310, 560, 95, 28))
        self.Tact_btn_2.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Tact_btn_2.setObjectName("Tact_btn_2")
        self.Power_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Power_btn_2.setGeometry(QtCore.QRect(310, 510, 95, 28))
        self.Power_btn_2.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.Power_btn_2.setObjectName("Power_btn_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 560, 261, 41))
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 270, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.image_comp_2 = QtWidgets.QLabel(self.centralwidget)
        self.image_comp_2.setGeometry(QtCore.QRect(430, 360, 231, 281))
        self.image_comp_2.setObjectName("image_comp_2")
        self.image_comp_2.raise_()
        self.image_comp.raise_()
        self.image_human.raise_()
        self.border_health_comp.raise_()
        self.Mellee_btn.raise_()
        self.Range_btn.raise_()
        self.Power_btn.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_stats_human.raise_()
        self.label_stats_comp.raise_()
        self.label_damage.raise_()
        self.label_attack_type.raise_()
        self.comp_name.raise_()
        self.human_name.raise_()
        self.border_health_human.raise_()
        self.healt_human.raise_()
        self.health_comp.raise_()
        self.Tact_btn.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.Range_btn_2.raise_()
        self.label_6.raise_()
        self.label_3.raise_()
        self.Mellee_btn_2.raise_()
        self.label_7.raise_()
        self.Tact_btn_2.raise_()
        self.Power_btn_2.raise_()
        self.label_8.raise_()
        self.pushButton.raise_()
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

        self.pushButton.setEnabled(False)

        if self.hero_h.intelligence + self.hero_h.durability >= self.hero_c.intelligence + self.hero_c.durability:
            self.disable_btns_c()
        else:
            if self.players ==2:
                self.disable_btns_h()
            else:
                self.comp_attack()


        if self.players == 1:
            self.Mellee_btn_2.setEnabled(False)
            self.Range_btn_2.setEnabled(False)
            self.Power_btn_2.setEnabled(False)
            self.Tact_btn_2.setEnabled(False)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_comp.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"image_c.jpg\"/></p></body></html>"))
        self.image_human.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"image_h.jpg\"/></p></body></html>"))
        self.Mellee_btn.setText(_translate("MainWindow", "Melee Atack"))
        self.Range_btn.setText(_translate("MainWindow", "Ranged Attack"))
        self.Power_btn.setText(_translate("MainWindow", "Power Up"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#000000;\">STR + CMB</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#000000;\">SPD + CMB</span></p></body></html>"))
        self.label_stats_human.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:9pt; color:#000000;\">STR: {self.hero_h.strength}</span></p><p><span style=\" font-size:9pt; color:#000000;\">SPD: {self.hero_h.speed}</span></p><p><span style=\" font-size:9pt; color:#000000;\">CMB: {self.hero_h.combat}</span></p><p><span style=\" font-size:9pt; color:#000000;\">POW: {self.hero_h.power}</span></p><p><span style=\" font-size:9pt; color:#000000;\">INT: {self.hero_h.intelligence}</span></p></body></html>"))
        self.label_stats_comp.setText(_translate("MainWindow", f"<html><head/><body><p align=\"right\"><span style=\" font-size:9pt; color:#000000;\">STR: {self.hero_c.strength}</span></p><p align=\"right\"><span style=\" font-size:9pt; color:#000000;\">SPD: {self.hero_c.speed}</span></p><p align=\"right\"><span style=\" font-size:9pt; color:#000000;\">CMB: {self.hero_c.combat}</span></p><p align=\"right\"><span style=\" font-size:9pt; color:#000000;\">POW: {self.hero_c.power}</span></p><p align=\"right\"><span style=\" font-size:9pt; color:#000000;\">INT: {self.hero_c.intelligence}</span></p></body></html>"))
        self.label_damage.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:9pt; color:#000000;\">{self.damage_msg}</span></p></body></html>"))
        self.label_attack_type.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:9pt; color:#000000;\">{self.attack_msg}</span></p></body></html>"))
        self.comp_name.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#000000;\">{self.hero_c.name.upper()}</span></p></body></html>"))
        self.human_name.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#000000;\">{self.hero_h.name.upper()}</span></p></body></html>"))
        self.Tact_btn.setText(_translate("MainWindow", "Tactitian"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#000000;\">INT + CMB bonus on defence &amp; next attack</span><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:8pt; color:#000000;\">POW + CMB bonus on defence &amp; next attack</span><br/></p></body></html>"))
        self.Range_btn_2.setText(_translate("MainWindow", "Ranged Attack"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:8pt; color:#000000;\"> bonus on defence &amp; next attack POW + CMB</span><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:8pt; color:#000000;\">STR + CMB</span></p></body></html>"))
        self.Mellee_btn_2.setText(_translate("MainWindow", "Melee Atack"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:8pt; color:#000000;\">SPD + CMB</span></p></body></html>"))
        self.Tact_btn_2.setText(_translate("MainWindow", "Tactitian"))
        self.Power_btn_2.setText(_translate("MainWindow", "Power Up"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:8pt; color:#000000;\">bonus on defence &amp; next attack INT + CMB</span><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.image_comp_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"VSBCK1.png\"/></p></body></html>"))

        self.Mellee_btn.clicked.connect(self.melee)
        self.Mellee_btn_2.clicked.connect(self.melee2)

        self.Range_btn.clicked.connect(self.range)
        self.Range_btn_2.clicked.connect(self.range2)

        self.Power_btn.clicked.connect(self.power_up)
        self.Power_btn_2.clicked.connect(self.power_up2)

        self.Tact_btn.clicked.connect(self.tact)
        self.Tact_btn_2.clicked.connect(self.tact2)

        self.pushButton.clicked.connect(self.ok_click)

    def fight(self, hero_attack, hero_deffence, attack_type):


        damage = hero_attack.attack(hero_deffence,attack_type)
        hero_deffence.health -= damage

        if attack_type != 'power_up' and attack_type != 'tactitian':
            self.attack_msg = f"{hero_attack.name} delt"
            self.damage_msg = f"{damage} DMG"
        elif attack_type == 'power_up':
            self.attack_msg = hero_attack.name
            self.damage_msg = f"POWERED UP {hero_attack.power_up}"
        elif attack_type == 'tactitian':
            self.attack_msg = hero_attack.name
            self.damage_msg = f"TACTITIAN {hero_attack.tactics}"

        _translate = QtCore.QCoreApplication.translate

        self.label_damage.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:9pt; color:#000000;\">{self.damage_msg}</span></p></body></html>"))
        self.label_attack_type.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:9pt; color:#000000;\">{self.attack_msg}</span></p></body></html>"))
       

        if hero_deffence.health <= 0:

            with open('image_w.jpg', 'wb') as img:
                img.write(hero_attack.image)


            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_WinnerWindow(hero_attack.health, hero_attack.name)
            self.ui.setupUi(self.window)
            self.MainWindow.hide()

            self.window.show()

        self.health_comp.setGeometry(QtCore.QRect(225, 80, self.hero_c.health, 14))
        self.healt_human.setGeometry(QtCore.QRect(671, 81, self.hero_h.health, 14))


    def disable_btns_h(self):
        self.Mellee_btn.setEnabled(False) 
        self.Range_btn.setEnabled(False) 
        self.Power_btn.setEnabled(False) 
        self.Tact_btn.setEnabled(False) 

        if self.players == 2:
            self.Mellee_btn_2.setEnabled(True) 
            self.Range_btn_2.setEnabled(True) 
            if self.hero_c.power_cnt >=3:
                self.Power_btn_2.setEnabled(True)
            if self.hero_c.tactics_cnt >=3: 
                self.Tact_btn_2.setEnabled(True) 

    def disable_btns_c(self):
        self.Mellee_btn_2.setEnabled(False) 
        self.Range_btn_2.setEnabled(False) 
        self.Power_btn_2.setEnabled(False) 
        self.Tact_btn_2.setEnabled(False) 

        self.Mellee_btn.setEnabled(True) 
        self.Range_btn.setEnabled(True) 
        if self.hero_h.power_cnt >=3:
            self.Power_btn.setEnabled(True)
        if self.hero_h.tactics_cnt >=3: 
            self.Tact_btn.setEnabled(True) 

    def enable_btn_ok(self):
        self.Mellee_btn.setEnabled(False) 
        self.Range_btn.setEnabled(False) 
        self.Power_btn.setEnabled(False) 
        self.Tact_btn.setEnabled(False) 
        self.pushButton.setEnabled(True)

    def ok_click(self):
        self.comp_attack()

        self.disable_btns_c()
        self.pushButton.setEnabled(False)

    def melee(self):
        self.fight(self.hero_h, self.hero_c, 'melee')
        if self.players == 2:
            self.disable_btns_h()
        else:
            self.enable_btn_ok()


    def melee2(self):
        self.fight(self.hero_c, self.hero_h, 'melee')
        if self.players == 2:
            self.disable_btns_c()

    def range(self):
        self.fight(self.hero_h, self.hero_c, 'ranged')
        if self.players == 2:
            self.disable_btns_h()
        else:
            self.enable_btn_ok()

    def range2(self):
        self.fight(self.hero_c, self.hero_h, 'ranged')
        if self.players == 2:
            self.disable_btns_c()

    def power_up(self):
        self.fight(self.hero_h, self.hero_c, 'power_up')
        if self.players == 2:
            self.disable_btns_h()
        else:
            self.enable_btn_ok()

    def power_up2(self):
        self.fight(self.hero_c, self.hero_h, 'power_up')
        if self.players == 2:
            self.disable_btns_c()

    def tact(self):
        self.fight(self.hero_h, self.hero_c, 'tactitian')
        if self.players == 2:
            self.disable_btns_h()
        else:
            self.enable_btn_ok()

    def tact2(self):
        self.fight(self.hero_c, self.hero_h, 'tactitian')
        if self.players == 2:
            self.disable_btns_c()

    def comp_attack(self):
        self.fight(self.hero_c, self.hero_h, self.hero_c.random_attack())



# import dc_rc
# import image_c_rc
# import image_h_rc

if __name__ == "__main__":
    import sys
    import pickle
    from random import randint
    from SuperHero import Hero 
    import os

    try:
        with open('heroes.pickle', 'rb') as heroes:
            all_heroes = pickle.load(heroes)
    except FileNotFoundError:
        command = 'python SuperHero.py'
        os.system(command)
        with open('heroes.pickle', 'rb') as heroes:
            all_heroes = pickle.load(heroes)
    
    hero_c = Hero.random_hero(all_heroes).hero_to_fight()

    hero_h = Hero.random_hero(all_heroes).hero_to_fight()

    with open('image_c.jpg', 'wb') as img:
        img.write(hero_c.image)

    with open('image_h.jpg', 'wb') as img:
        img.write(hero_h.image)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(hero_c, hero_h, 2, MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

