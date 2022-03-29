# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'INTERFACE7.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import cv2
from dronekit import connect , Command
from pymavlink import mavutil
import numpy as np


class Ui_MainWindow(object):
    def __init__(self):
        self.video_size = QSize(640, 480)
        self.harita = 0
        self.setup_camera()
        self.hedef_gosterme_hazirlik()
        self.ihalar = [5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.iha_lat , self.iha_lon = 40.230758, 29.008734
        self.lat = [self.iha_lat, 40.230758, 40.232183, 40.231528, 40.232191, 40.232502, 40.229656, 40.233362,
                    40.229337]
        self.lon = [self.iha_lon, 29.008219, 29.008734, 29.008026, 29.004861, 29.010472, 29.007967, 29.007752,
                    29.007972]

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 1070)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(730, 630, 69, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(730, 600, 121, 16))
        self.KAMIKAZEHAZIRLIK = QPushButton(self.centralwidget)
        self.KAMIKAZEHAZIRLIK.setObjectName(u"KAMIKAZEHAZIRLIK")
        self.KAMIKAZEHAZIRLIK.setGeometry(QRect(730, 700, 111, 23))
        self.KAMIKAZEDALIS = QPushButton(self.centralwidget)
        self.KAMIKAZEDALIS.setObjectName(u"KAMIKAZEDALIS")
        self.KAMIKAZEDALIS.setGeometry(QRect(730, 730, 101, 23))
        self.iha_durum = QLineEdit(self.centralwidget)
        self.iha_durum.setObjectName(u"iha_durum")
        self.iha_durum.setGeometry(QRect(670, 63, 113, 20))
        self.baglanti = QPushButton(self.centralwidget)
        self.baglanti.setObjectName(u"baglanti")
        self.baglanti.setStyleSheet(u"background-color : red")
        self.baglanti.setGeometry(QRect(670, 35, 101, 23))
        self.iha_durum_2 = QLineEdit(self.centralwidget)
        self.iha_durum_2.setObjectName(u"iha_durum_2")
        self.iha_durum_2.setGeometry(QRect(670, 10, 113, 20))
        self.goruntu = QLabel(self.centralwidget)
        self.goruntu.setObjectName(u"goruntu")
        self.goruntu.setGeometry(QRect(10, 10, 640, 480))
        self.goruntu_2 = QLabel(self.centralwidget)
        self.goruntu_2.setObjectName(u"goruntu_2")
        self.goruntu_2.setGeometry(QRect(10, 500, 700, 550))
        self.KAMIKAZEDALIS_2 = QPushButton(self.centralwidget)
        self.KAMIKAZEDALIS_2.setObjectName(u"KAMIKAZEDALIS_2")
        self.KAMIKAZEDALIS_2.setGeometry(QRect(730, 530, 121, 23))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(730, 500, 121, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        # BUTONLAR
        self.baglanti.clicked.connect(self.iha_baglan_buton)
        self.KAMIKAZEHAZIRLIK.clicked.connect(self.kamikaze_hazirlik_buton)
        self.KAMIKAZEDALIS_2.clicked.connect(self.harita_secimi_buton)
        # BUTONLAR

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"NOKTA 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"NOKTA 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"NOKTA 3", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"NOKTA 4", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"NOKTA 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KAMIKAZE SECENEKLERI", None))
        self.KAMIKAZEHAZIRLIK.setText(QCoreApplication.translate("MainWindow", u"KAMIKAZE HAZIRLIK", None))
        self.KAMIKAZEDALIS.setText(QCoreApplication.translate("MainWindow", u"KAMIKAZE DALIS", None))
        self.baglanti.setText(QCoreApplication.translate("MainWindow", u"IHA'YA BAGLAN", None))
        self.iha_durum_2.setText(QCoreApplication.translate("MainWindow", u"tcp:127.0.0.1:5762", None))
        self.goruntu.setText(QCoreApplication.translate("MainWindow", u"DODO", None))
        self.goruntu_2.setText(QCoreApplication.translate("MainWindow", u"DODO", None))
        self.KAMIKAZEDALIS_2.setText(QCoreApplication.translate("MainWindow", u"Harita Secimi Yap", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"HEDEF IHA HARITA", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"KAMIKAZE HARITA", None))

        self.comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"HEDEF IHA HARITA", None))
    # retranslateUi
        self.baglanti_sayac = 0
        self.hedef_lat = [40.233100, 40.231331, 40.229251, 40.231986]
        self.hedef_lon = [29.001739, 29.007768, 29.009313, 29.010343]

    def harita_secimi_buton(self):
        if (self.comboBox_2.currentText() == "HEDEF IHA HARITA"):
            self.harita = 0
        else : self.harita =1


    def iha_baglan_buton(self):
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

    def kamikaze_hazirlik_buton(self):
        if self.baglanti_sayac > 0:
            sayac = int(self.comboBox.currentText()[5:])
            print(self.hedef_lat[sayac - 1], self.hedef_lon[sayac - 1])

            self.cmds = self.vehicle.commands
            self.cmds.download()
            self.cmds.wait_ready()
            self.cmds.clear()

            self.cmd1 = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                                mavutil.mavlink.MAV_CMD_NAV_LOITER_UNLIM, 0,
                                0, 0, 0, 100, 0, self.hedef_lat[sayac - 1], self.hedef_lon[sayac - 1], 100)

            self.cmds.add(self.cmd1)
            self.cmds.upload()
            self.vehicle.mode = "FBWA"
            self.vehicle.mode = "AUTO"

    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()

        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(30)
    def hedef_gosterme_hazirlik(self):
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.display_harita)
        self.timer2.start(30)

    def display_harita(self):
        frame = hedef_harita(self.ihalar,self.lat,self.lon)
        self.iha_lat , self.iha_lon = self.iha_koordinat_al()
        frame2 = kamikaze_harita(self.iha_lat,self.iha_lon)
        if self.harita == 0:
            frame = frame
        else : frame = frame2
        frame = cv2.resize(frame,(700,550))
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self.goruntu_2.setPixmap(QPixmap.fromImage(image))
    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        self.iha_lat, self.iha_lon = self.iha_koordinat_al()
        self.lat[0] = self.iha_lat
        self.lon[0] = self.iha_lon
        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame,  cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self.goruntu.setPixmap(QPixmap.fromImage(image))
    def iha_koordinat_al(self):
        if self.baglanti_sayac > 0:
            return self.vehicle.location.global_relative_frame.lat, self.vehicle.location.global_relative_frame.lon
        else:
            return 40.230618, 29.006524

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
    image = cv2.resize(image,(640,480))
    return image

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
    image = cv2.resize(image,(640,480))
    return image

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