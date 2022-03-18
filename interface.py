# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'INTERFACE.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dronekit import connect , Command
from pymavlink import mavutil
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 193)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 30, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 121, 16))
        self.label.setObjectName("label")
        self.KAMIKAZEHAZIRLIK = QtWidgets.QPushButton(self.centralwidget)
        self.KAMIKAZEHAZIRLIK.setGeometry(QtCore.QRect(210, 90, 131, 23))
        self.KAMIKAZEHAZIRLIK.setObjectName("KAMIKAZEHAZIRLIK")
        self.KAMIKAZEDALIS = QtWidgets.QPushButton(self.centralwidget)
        self.KAMIKAZEDALIS.setGeometry(QtCore.QRect(210, 120, 131, 23))
        self.KAMIKAZEDALIS.setObjectName("KAMIKAZEDALIS")
        self.iha_durum = QtWidgets.QLineEdit(self.centralwidget)
        self.iha_durum.setGeometry(QtCore.QRect(50, 70, 113, 20))
        self.iha_durum.setObjectName("iha_durum")
        self.baglanti = QtWidgets.QPushButton(self.centralwidget)
        self.baglanti.setGeometry(QtCore.QRect(330, 20, 101, 23))
        self.baglanti.setObjectName("baglanti")
        self.baglanti.setStyleSheet("background-color : red")
        self.iha_durum_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.iha_durum_2.setGeometry(QtCore.QRect(210, 20, 113, 20))
        self.iha_durum_2.setObjectName("iha_durum_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #BUTONLAR
        self.baglanti.clicked.connect(self.iha_baglan)
        self.KAMIKAZEHAZIRLIK.clicked.connect(self.kamikaze_hazirlik)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setCurrentText(_translate("MainWindow", "NOKTA 1"))
        self.comboBox.setItemText(0, _translate("MainWindow", "NOKTA 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "NOKTA 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "NOKTA 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "NOKTA 4"))
        self.label.setText(_translate("MainWindow", "KAMIKAZE SECENEKLERI"))
        self.KAMIKAZEHAZIRLIK.setText(_translate("MainWindow", "KAMIKAZE HAZIRLIK"))
        self.KAMIKAZEDALIS.setText(_translate("MainWindow", "KAMIKAZE DALIS"))
        self.baglanti.setText(_translate("MainWindow", "IHA\'YA BAGLAN"))
        self.iha_durum_2.setText(_translate("MainWindow", "tcp:127.0.0.1:5762"))
        self.baglanti_sayac = 0
        self.hedef_lat = [40.233100, 40.229447, 40.229251, 40.231986]
        self.hedef_lon = [29.001739, 29.002554, 29.009313, 29.010343]

    def iha_baglan(self):
        if len(self.iha_durum_2.text())<1:
            msg = QMessageBox()
            msg.setWindowTitle("BAGLANTI UYARISI")
            msg.setText("GECERLI BIR BAGLANTI IP'SI GIRIN")
            msg.setIcon(QMessageBox.Critical)
            x=msg.exec_()
        if self.baglanti_sayac == 0:
            self.vehicle = connect(self.iha_durum_2.text(), wait_ready=True)
            self.baglanti.setStyleSheet("background-color : green")
            self.baglanti_sayac+=1
        else :
            msg = QMessageBox()
            msg.setWindowTitle("BAGLANTI UYARISI")
            msg.setText("CIHAZLA BAGLANTI ZATEN VAR")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
            self.iha_durum.setText(str(self.vehicle.mode))


    def kamikaze_hazirlik(self):
        if self.baglanti_sayac > 0:
            self.kamikaze_hazirlik_sec(self.comboBox.currentText())
    def kamikaze_hazirlik_sec(self,hedef):
        sayac = int(hedef[5:])
        print(self.hedef_lat[sayac-1],self.hedef_lon[sayac-1])

        self.cmds = self.vehicle.commands
        self.cmds.download()
        self.cmds.wait_ready()
        self.cmds.clear()

        self.cmd1 = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_LOITER_UNLIM, 0,
                       0, 0, 0, 250, 0, self.hedef_lat[sayac-1], self.hedef_lon[sayac-1], 100)

        self.cmds.add(self.cmd1)
        self.cmds.upload()
        self.vehicle.mode = "FBWA"
        self.vehicle.mode = "AUTO"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    print("dongu")
    sys.exit(app.exec_())

