# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WINNER.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WinnerWindow(object):

    def __init__(self, hero):
        self.health = hero.health

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(794, 606)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(320, 210, 161, 251))
        self.label_img.setObjectName("label_img")
        self.label_health = QtWidgets.QLabel(self.centralwidget)
        self.label_health.setGeometry(QtCore.QRect(290, 190, 221, 16))
        self.label_health.setStyleSheet("color: rgb(255, 0, 4);\n"
"background-color: rgb(255, 0, 4);\n"
"background-color: rgb(212, 0, 3);")
        self.label_health.setObjectName("label_health")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 40, 371, 101))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 26))
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
        self.label_img.setText(_translate("MainWindow", "<html><head/><body><p><img src=\"image_w.jpg\"/></p></body></html>"))
        self.label_health.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#f8e801;\">WINNER!</span></p></body></html>"))

# import image_c_rc
# import image_h_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_WinnerWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

