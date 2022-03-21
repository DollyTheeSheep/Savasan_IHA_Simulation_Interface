# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'INTERFACE5.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
from dronekit import connect , Command
from pymavlink import mavutil
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1842, 716)
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
        self.KAMIKAZEHAZIRLIK.setGeometry(QtCore.QRect(210, 70, 131, 23))
        self.KAMIKAZEHAZIRLIK.setObjectName("KAMIKAZEHAZIRLIK")
        self.KAMIKAZEDALIS = QtWidgets.QPushButton(self.centralwidget)
        self.KAMIKAZEDALIS.setGeometry(QtCore.QRect(210, 95, 131, 23))
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
        self.goruntu = QtWidgets.QLabel(self.centralwidget)
        self.goruntu.setGeometry(QtCore.QRect(10, 130, 1800, 550))
        self.goruntu.setObjectName("goruntu")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # GORUNTU
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        # BUTONLAR
        self.baglanti.clicked.connect(self.iha_baglan)
        self.KAMIKAZEHAZIRLIK.clicked.connect(self.kamikaze_hazirlik)
        # GORUNTU

    def ImageUpdateSlot(self, Image):
        self.goruntu.setPixmap(QPixmap.fromImage(Image))

    def CancelFeed(self):
        self.Worker1.stop()
    # END GORUNTU


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
        self.goruntu.setText(_translate("MainWindow", "DODO"))

        self.baglanti_sayac = 0
        self.hedef_lat = [40.233100, 40.229447, 40.229251, 40.231986]
        self.hedef_lon = [29.001739, 29.002554, 29.009313, 29.010343]

    def iha_baglan(self):
        if len(self.iha_durum_2.text()) < 1:
            msg = QMessageBox()
            msg.setWindowTitle("BAGLANTI UYARISI")
            msg.setText("GECERLI BIR BAGLANTI IP'SI GIRIN")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
        if self.baglanti_sayac == 0:
            self.vehicle = connect(self.iha_durum_2.text(), wait_ready=True)
            self.baglanti.setStyleSheet("background-color : green")
            self.baglanti_sayac += 1
        else:
            msg = QMessageBox()
            msg.setWindowTitle("BAGLANTI UYARISI")
            msg.setText("CIHAZLA BAGLANTI ZATEN VAR")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
            self.iha_durum.setText(str(self.vehicle.mode))

    def kamikaze_hazirlik(self):
        if self.baglanti_sayac > 0:
            hedef = self.comboBox.currentText()
            sayac = int(hedef[5:])
            print(self.hedef_lat[sayac - 1], self.hedef_lon[sayac - 1])

            self.cmds = self.vehicle.commands
            self.cmds.download()
            self.cmds.wait_ready()
            self.cmds.clear()

            self.cmd1 = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                                mavutil.mavlink.MAV_CMD_NAV_LOITER_UNLIM, 0,
                                0, 0, 0, 250, 0, self.hedef_lat[sayac - 1], self.hedef_lon[sayac - 1], 100)

            self.cmds.add(self.cmd1)
            self.cmds.upload()
            self.vehicle.mode = "FBWA"
            self.vehicle.mode = "AUTO"

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        self.ThreadActive = True
        ihalar = [5, 6, 7, 8, 9, 10, 11, 12, 13]
        lat = [40.231478, 40.230758, 40.232183, 40.231528, 40.232191, 40.232502, 40.229656, 40.233362, 40.229337]
        lon = [29.006931, 29.008219, 29.008734, 29.008026, 29.004861, 29.010472, 29.007967, 29.007752, 29.007972]
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = hedef_harita(ihalar,lat,lon)
            ret2, frame2 = Capture.read()
            ret3, frame3 = kamikaze_harita(lat[0],lon[0])
            if ret and ret2 and ret3:
                Image = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                #fotolari birlestirme
                Image =  np.hstack((frame,FlippedImage))
                Image = np.hstack((Image,frame3))
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0],
                                           QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(QSize(1800, 550), Qt.IgnoreAspectRatio)
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()
def kamikaze_harita(lat,lon):
    # yarisma zamani kamikaze noktalari alindigi zaman buraya array olarak koordinatlari eklenecek

    kamikaze_latlar = [lat,40.230618,40.232674,40.232766]
    kamikaze_lonlar = [lon,29.006524,29.006567,29.008873]
    sayi = len(kamikaze_latlar)


    image = cv2.imread('700x550.png')
    cv2.putText(image, "KAMIKAZE HEDEFLER", (290, 30), 1, 1, (0, 0, 0), 2)
    cv2.rectangle(image, (100, 100), (600, 450), (255, 0, 0), 1)

    for i in range (sayi):
        kamikaze_x,kamikaze_y = lat_lon_to_pixel(kamikaze_latlar[i],kamikaze_lonlar[i])
        if kamikaze_x>0:kamikaze_x = kamikaze_x+100
        if kamikaze_y>0:kamikaze_y= (350-kamikaze_y) + 100

        if kamikaze_x > 700 : kamikaze_x = 700
        if kamikaze_x < 0 and kamikaze_x > -100 : kamikaze_x = kamikaze_x*(-1)
        if kamikaze_x <= -100: kamikaze_x = 0

        if kamikaze_y > 550 : kamikaze_y = 550
        if kamikaze_y < 0 and kamikaze_y > -100 : kamikaze_y = (kamikaze_y*(-1)) + 450
        if kamikaze_y < -100: kamikaze_y = 550

        center = (kamikaze_x, kamikaze_y)

        if i == 0:
            cv2.circle(image, center, 2, (0, 255, 0), 2, cv2.LINE_8, 0)
            cv2.putText(image, "ACE", (kamikaze_x - 15, kamikaze_y - 5), 1, 1, (0, 255, 0), 1)
        else:
            cv2.circle(image, center, 2, (0, 0, 255), 2, cv2.LINE_8, 0)
            cv2.putText(image, "KMKZ-" + str(i), (kamikaze_x - 20, kamikaze_y - 5), 1, 1, (0, 0, 255), 1)
    ret = True
    image = cv2.resize(image,(640,480))
    return ret, image

def hedef_harita(ihalar, lat, lon):
    sayi = len(ihalar)
    image = cv2.imread('700x550.png')
    cv2.putText(image, "HEDEF IHALAR", (290, 30), 1, 1, (0, 0, 0), 2)
    cv2.rectangle(image, (100, 100), (600, 450), (255, 0, 0), 1)

    for i in range(sayi):
        x, y = lat_lon_to_pixel(lat[i], lon[i])

        if x > 0: x = x + 100
        if y > 0: y = (350 - y) + 100

        if x > 700: x = 700
        if x < 0 and x > -100: x = x * (-1)
        if x <= -100: x = 0

        if y > 550: y = 550
        if y < 0 and y > -100: y = (y * (-1)) + 450
        if y < -100: y = 550

        center = (x, y)

        if i == 0:
            cv2.circle(image, center, 2, (0, 255, 0), 2, cv2.LINE_8, 0)
            cv2.putText(image, "ACE", (x - 15, y - 5), 1, 1, (0, 255, 0), 1)
        else:
            cv2.circle(image, center, 2, (0, 0, 255), 2, cv2.LINE_8, 0)
            cv2.putText(image, "D" + str(ihalar[i]), (x - 10, y - 5), 1, 1, (0, 0, 255), 1)
        ret2=True
    image = cv2.resize(image,(640,480))
    return ret2,image

def lat_lon_to_pixel(lat, lon):
    harita_piksel_x, harita_piksel_y = 500, 350
    # sag ust sol ust sol alt sag alt
    sinirlar_lat = [40.233108, 40.233076, 40.229885, 40.229857]
    # sag ust sol ust sol alt sag alt
    sinirlar_lon = [29.009710, 29.005740, 29.005698, 29.009774]
    en_sag_lon = 29.009774
    en_sol_lon = 29.005698
    en_ust_lat = 40.233108
    en_alt_lat = 40.229857
    lonlar_fark = en_sag_lon - en_sol_lon
    latlar_fark = en_ust_lat - en_alt_lat

    sonuc_lon = lon - en_sol_lon
    sonuc_lat = lat - en_alt_lat

    sonuc_piksel_x = sonuc_lon / lonlar_fark * 500
    sonuc_piksel_y = sonuc_lat / latlar_fark * 350

    return int(sonuc_piksel_x), int(sonuc_piksel_y)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

