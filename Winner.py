# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'winner2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WinnerWindow(object):

    def __init__(self, health = 200, hero_name = 'PLAYER'):
        self.health =int(health)
        self.hero_name = hero_name


    def setupUi(self, WinnerWindow):
        WinnerWindow.setObjectName("WinnerWindow")
        WinnerWindow.setEnabled(True)
        WinnerWindow.resize(794, 606)
        WinnerWindow.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.centralwidget = QtWidgets.QWidget(WinnerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(335, 60, 161, 241))
        self.label_img.setObjectName("label_img")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 301, 71))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 130, 301, 71))
        self.label_4.setObjectName("label_4")
        self.border_health_comp = QtWidgets.QLabel(self.centralwidget)
        self.border_health_comp.setGeometry(QtCore.QRect(314, 29, 202, 16))
        self.border_health_comp.setStyleSheet("color: rgb(0, 0, 4);\n"
"background-color: rgb(255, 0, 0);\n"
"background-color: rgb(240,240, 240);")
        self.border_health_comp.setFrameShape(QtWidgets.QFrame.Box)
        self.border_health_comp.setText("")
        self.border_health_comp.setObjectName("border_health_comp")
        self.health_comp = QtWidgets.QLabel(self.centralwidget)
        self.health_comp.setGeometry(QtCore.QRect(315, 30, self.health, 14))
        self.health_comp.setToolTipDuration(1)
        self.health_comp.setStyleSheet("color: rgb(255, 0, 4);\n"
"background-color: rgb(255, 0, 4);\n"
"background-color: rgb(212, 0, 3);")
        self.health_comp.setText("")
        self.health_comp.setObjectName("health_comp")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 300, 781, 421))
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_img.raise_()
        self.label_3.raise_()
        self.border_health_comp.raise_()
        self.health_comp.raise_()
        WinnerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WinnerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
        self.menubar.setObjectName("menubar")
        WinnerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WinnerWindow)
        self.statusbar.setObjectName("statusbar")
        WinnerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WinnerWindow)
        QtCore.QMetaObject.connectSlotsByName(WinnerWindow)

    def retranslateUi(self, WinnerWindow):
        _translate = QtCore.QCoreApplication.translate
        WinnerWindow.setWindowTitle(_translate("WinnerWindow", "MainWindow"))
        self.label_img.setText(_translate("WinnerWindow", "<html><head/><body><p><img src=\"image_w.jpg\"/></p></body></html>"))
        self.label_3.setText(_translate("WinnerWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#515151;\">{self.hero_name}</span></p></body></html>"))
        self.label_4.setText(_translate("WinnerWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:40pt; color:#515151;\">WINS!</span></p></body></html>"))
        self.label.setText(_translate("WinnerWindow", "<html><head/><body><p><img src=\"winner_bck.png\"/></p></body></html>"))

# import bck_rc
# import image_c_rc
# import image_h_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WinnerWindow = QtWidgets.QMainWindow()
    ui = Ui_WinnerWindow()
    ui.setupUi(WinnerWindow)
    WinnerWindow.show()
    sys.exit(app.exec_())

