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
from dronekit import connect , Command , LocationGlobalRelative, LocationGlobal
from pymavlink import mavutil
import numpy as np
import math
import receive

class Ui_MainWindow(object):
    def __init__(self):
        self.video_size = QSize(640, 480)
        self.harita = 0
        self.temp = 0
        self.kamikaze_hazirlik_on = 0
        self.donus_sayaci = 0
        self.location_current = LocationGlobalRelative(0, 0, 0)
        self.att_heading_deg = 0.0
        self.kamikaze_dalis()
        self.setup_camera()
        self.hedef_gosterme_hazirlik()
        self.ihalar = [5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.iha_lat , self.iha_lon = 40.230758, 29.008734
        self.lat = [self.iha_lat, 40.2314011, 40.232183, 40.231528, 40.232191, 40.232502, 40.229656, 40.233362,
                    40.229337]
        self.lon = [self.iha_lon, 29.0094370, 29.008734, 29.008026, 29.004861, 29.010472, 29.007967, 29.007752,
                    29.007972]
        self.haberlesme = receive.haberlesme()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 1070)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox2 = QComboBox(self.centralwidget)
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        #self.comboBox.addItem("")
        self.comboBox2.setObjectName(u"comboBox2")
        self.comboBox2.setGeometry(QRect(730, 580, 125, 22))

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(730, 735, 125, 23))

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(730, 600, 121, 16))
        self.label2 = QLabel(self.centralwidget)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(670, 90, 121, 16))
        self.label3 = QLabel(self.centralwidget)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(670, 120, 121, 16))
        self.label4 = QLabel(self.centralwidget)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QRect(670, 150, 121, 16))
        self.label5 = QLabel(self.centralwidget)
        self.label5.setObjectName(u"label5")
        self.label5.setGeometry(QRect(670, 175, 175, 300))
        self.label6 = QLabel(self.centralwidget)
        self.label6.setObjectName(u"label6")
        self.label6.setGeometry(QRect(730, 755, 175, 22))
        self.IHATAKIP = QPushButton(self.centralwidget)
        self.IHATAKIP.setObjectName(u"IHATAKIP")
        self.IHATAKIP.setGeometry(QRect(730, 630, 125, 23))
        self.IHATAKIPBIRAK = QPushButton(self.centralwidget)
        self.IHATAKIPBIRAK.setObjectName(u"IHATAKIPBIRAK")
        self.IHATAKIPBIRAK.setGeometry(QRect(730, 660, 125, 23))
        self.KAMIKAZEHAZIRLIK = QPushButton(self.centralwidget)
        self.KAMIKAZEHAZIRLIK.setObjectName(u"KAMIKAZEHAZIRLIK")
        self.KAMIKAZEHAZIRLIK.setGeometry(QRect(730, 790, 125, 23))
        self.KAMIKAZEDALIS = QPushButton(self.centralwidget)
        self.KAMIKAZEDALIS.setObjectName(u"KAMIKAZEDALIS")
        self.KAMIKAZEDALIS.setGeometry(QRect(730, 820, 125, 23))
        self.KAMIKAZEIPTAL = QPushButton(self.centralwidget)
        self.KAMIKAZEIPTAL.setObjectName(u"KAMIKAZEIPTAL")
        self.KAMIKAZEIPTAL.setGeometry(QRect(730, 850, 125, 23))
        #self.iha_durum = QLineEdit(self.centralwidget)
        #self.iha_durum.setObjectName(u"iha_durum")
        #self.iha_durum.setGeometry(QRect(670, 63, 113, 20))
        self.baglanti = QPushButton(self.centralwidget)
        self.baglanti.setObjectName(u"baglanti")
        self.baglanti.setStyleSheet(u"background-color : red")
        self.baglanti.setGeometry(QRect(670, 35, 101, 23))
        self.iha_durum_2 = QLineEdit(self.centralwidget)
        self.iha_durum_2.setObjectName(u"iha_durum_2")
        self.iha_durum_2.setGeometry(QRect(670, 10, 113, 20))
        self.ucus_mod = QLineEdit(self.centralwidget)
        self.ucus_mod.setObjectName(u"ucus_mod")
        self.ucus_mod.setGeometry(QRect(745, 88, 100, 20))
        self.ucus_hiz = QLineEdit(self.centralwidget)
        self.ucus_hiz.setObjectName(u"ucus_mod")
        self.ucus_hiz.setGeometry(QRect(745, 118, 100, 20))
        self.bas_acisi = QLineEdit(self.centralwidget)
        self.bas_acisi.setObjectName(u"bas_acisi")
        self.bas_acisi.setGeometry(QRect(745, 148, 100, 20))
        self.goruntu = QLabel(self.centralwidget)
        self.goruntu.setObjectName(u"goruntu")
        self.goruntu.setGeometry(QRect(10, 10, 640, 480))
        self.goruntu_2 = QLabel(self.centralwidget)
        self.goruntu_2.setObjectName(u"goruntu_2")
        self.goruntu_2.setGeometry(QRect(10, 500, 700, 550))
        """self.KAMIKAZEDALIS_2 = QPushButton(self.centralwidget)
        self.KAMIKAZEDALIS_2.setObjectName(u"KAMIKAZEDALIS_2")
        self.KAMIKAZEDALIS_2.setGeometry(QRect(730, 530, 125, 23))
        """

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
        #self.KAMIKAZEDALIS_2.clicked.connect(self.harita_secimi_buton)
        self.KAMIKAZEDALIS.clicked.connect(self.kamikaze_dalis_buton)
        self.KAMIKAZEIPTAL.clicked.connect(self.kamikaze_iptal_buton)
        self.IHATAKIP.clicked.connect(self.iha_takip)
        self.IHATAKIPBIRAK.clicked.connect(self.iha_takip_birak)
        # BUTONLAR

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ACE ARAYUZ", None))
        #self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"D 6", None))
        self.comboBox2.setItemText(0, QCoreApplication.translate("MainWindow", u"D 7", None))
        self.comboBox2.setItemText(1, QCoreApplication.translate("MainWindow", u"D 8", None))
        self.comboBox2.setItemText(2, QCoreApplication.translate("MainWindow", u"D 9", None))
        self.comboBox2.setItemText(3, QCoreApplication.translate("MainWindow", u"D 10", None))
        self.comboBox2.setItemText(4, QCoreApplication.translate("MainWindow", u"D 11", None))
        self.comboBox2.setItemText(5, QCoreApplication.translate("MainWindow", u"D 12", None))
        self.comboBox2.setItemText(6, QCoreApplication.translate("MainWindow", u"D 13", None))
        self.comboBox2.setCurrentText(QCoreApplication.translate("MainWindow", u"DUSMAN", None))

        #self.pixmap = cv2.imread("imza4.png")
        #self.pixmap = cv2.resize(self.pixmap,(175,300))
        #cv2.imwrite("imza5.jpg",self.pixmap)
        self.pixmap = QPixmap("imza5.jpg")
        self.label5.setPixmap(self.pixmap)

        self.label.setText(QCoreApplication.translate("MainWindow", u"HEDEF IHA SECENEKLERI", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"UCUS MODU : ", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"UCUS HIZI : ", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"BAS ACISI : ", None))
        self.label6.setText(QCoreApplication.translate("MainWindow", u"HAZIRLIK CEMBER SECIMI", None))
        self.KAMIKAZEHAZIRLIK.setText(QCoreApplication.translate("MainWindow", u"KAMIKAZE HAZIRLIK", None))
        self.KAMIKAZEDALIS.setText(QCoreApplication.translate("MainWindow", u"KAMIKAZE DALIS", None))
        self.KAMIKAZEIPTAL.setText(QCoreApplication.translate("MainWindow", u"KAMIKAZE IPTAL", None))
        self.IHATAKIP.setText(QCoreApplication.translate("MainWindow", u"HEDEFI TAKIP ET", None))
        self.IHATAKIPBIRAK.setText(QCoreApplication.translate("MainWindow", u"HEDEFI TAKIBI BIRAK", None))
        self.baglanti.setText(QCoreApplication.translate("MainWindow", u"IHA'YA BAGLAN", None))
        self.iha_durum_2.setText(QCoreApplication.translate("MainWindow", u"tcp:127.0.0.1:5762", None))
        self.ucus_mod.setText(QCoreApplication.translate("MainWindow", u"AUTO", None))
        self.ucus_hiz.setText(QCoreApplication.translate("MainWindow", u"20 m/s", None))
        self.bas_acisi.setText(QCoreApplication.translate("MainWindow", u"120", None))
        self.goruntu.setText(QCoreApplication.translate("MainWindow", u"DODO", None))
        self.goruntu_2.setText(QCoreApplication.translate("MainWindow", u"DODO", None))
        #self.KAMIKAZEDALIS_2.setText(QCoreApplication.translate("MainWindow", u"Harita Secimi Yap", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"KUZEY NOKTASI", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"GUNEY NOKTASI", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"DOGU NOKTASI", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"BATI NOKTASI", None))

        #self.comboBox_2.setCurrentText(QCoreApplication.translate("MainWindow", u"HEDEF IHA HARITA", None))
    # retranslateUi
        self.baglanti_sayac = 0
        self.hedef_lat = [40.233100, 40.231331, 40.229251, 40.231986]
        self.hedef_lon = [29.001739, 29.007768, 29.009313, 29.010343]

    """def harita_secimi_buton(self):
        if (self.comboBox_2.currentText() == "HEDEF IHA HARITA"):
            self.harita = 0
        else : self.harita =1"""


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
            #self.iha_durum.setText(str(self.vehicle.mode))

    def kamikaze_hazirlik_buton(self):
        print("kamikaze hazirlik buton")
        if self.baglanti_sayac > 0:
            hedef_lat = self.lat[1]
            hedef_lon = self.lon[1]
            self.lat_70m = 0.0006287
            self.lon_70m = 0.0008342
            self.lat_200m = 0.0018092
            self.lon_200m = 0.0023497
            self.hazirlik_yon = self.comboBox_2.currentText()[0:1]
            print(self.hazirlik_yon)
            if self.hazirlik_yon[0:1] == "K":
                self.hazirlik_noktasi = round(hedef_lat+self.lat_200m,7), round(hedef_lon + self.lon_70m,7) ,1
                print("Hazirlik Kuzey")

            elif self.hazirlik_yon[0:1] == "G":
                self.hazirlik_noktasi = round(hedef_lat-self.lat_200m,7), round(hedef_lon - self.lon_70m,7), 2
                print("Hazirlik Guney")
            elif self.hazirlik_yon[0:1] == "D":
                self.hazirlik_noktasi = round(hedef_lat - self.lat_70m,7), round(hedef_lon + self.lon_200m,7), 3
                print("Hazirlik Dogu")
            else:
                self.hazirlik_noktasi = round(hedef_lat + self.lat_70m, 7), round(hedef_lon - self.lon_200m, 7), 4
                print("Hazirlik Batı")

            self.cmds = self.vehicle.commands
            self.cmds.download()
            self.cmds.wait_ready()
            self.cmds.clear()
            self.hazirlik_lat = 0
            self.hazirlik_lon = 0
            cmd1 = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                                mavutil.mavlink.MAV_CMD_NAV_LOITER_UNLIM, 0,
                                0, 0, 0, -63, 0, self.hazirlik_noktasi[0], self.hazirlik_noktasi[1], 110)

            self.cmds.add(cmd1)
            self.cmds.upload()
            self.vehicle.mode = "FBWA"
            self.vehicle.mode = "AUTO"
            self.kamikaze_hazirlik_on = 1

    def kamikaze_dalis_buton(self):
        print("kamikaze dalis buton")
        if self.hazirlik_noktasi[2] == 1:
            dalis_path_lat = self.hazirlik_noktasi[0]
            dalis_path_lon = self.hazirlik_noktasi[1]-self.lon_70m
        elif self.hazirlik_noktasi[2] == 2:
            dalis_path_lat = self.hazirlik_noktasi[0]
            dalis_path_lon = self.hazirlik_noktasi[1] + self.lon_70m
        elif self.hazirlik_noktasi[2] == 3:
            dalis_path_lat = self.hazirlik_noktasi[0] + self.lat_70m
            dalis_path_lon = self.hazirlik_noktasi[1]
        elif self.hazirlik_noktasi[2] == 4:
            dalis_path_lat = self.hazirlik_noktasi[0] - self.lat_70m
            dalis_path_lon = self.hazirlik_noktasi[1]

        self.cmds.clear()
        cmd = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                       mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0,
                       0, 0, 0, 0, 0, dalis_path_lat, dalis_path_lon, 110)
        cmd2 = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
                      mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0,
                      0, 0, 0, 0, 0, self.lat[1], self.lon[1], 110)
        self.cmds.add(cmd)
        self.cmds.add(cmd2)
        self.cmds.upload()
        self.vehicle.mode = "FBWA"
        self.vehicle.mode = "AUTO"
        if self.baglanti_sayac > 0 and self.kamikaze_hazirlik_on > 0 :
            self.timer3.start(30)

    """
        self.temp = 0
        self.vehicle.mode = "GUIDED"
        self.turn_heading("r", 90, 110)
        if self.baglanti_sayac > 0 and self.kamikaze_hazirlik_on > 0 and self.donus_sayaci > 0:
            self.timer3.start(30)"""

    def kamikaze_iptal_buton(self):

        print("kamikaze iptal buton")
        self.send_attitude_target(0, 45, 0, thrust=0)
        self.vehicle.mode = "AUTO"
        self.timer3.stop()
        print("kamikaze iptal")
    def iha_takip(self):
        print("IHA TAKIP")
        pass
    def iha_takip_birak(self):
        print("IHA TAKIP BIRAK")
        pass


    def send_attitude_target(self, roll_angle=0.0, pitch_angle=0.0,
                             yaw_angle=None, yaw_rate=0.0, use_yaw_rate=False,
                             thrust=0.5):
        """
        use_yaw_rate: the yaw can be controlled using yaw_angle OR yaw_rate.
                      When one is used, the other is ignored by Ardupilot.
        thrust: 0 <= thrust <= 1, as a fraction of maximum vertical thrust.
                Note that as of Copter 3.5, thrust = 0.5 triggers a special case in
                the code for maintaining current altitude.
        """
        if yaw_angle is None:
            # this value may be unused by the vehicle, depending on use_yaw_rate
            yaw_angle = self.vehicle.attitude.yaw
        # Thrust >  0.5: Ascend
        # Thrust == 0.5: Hold the altitude
        # Thrust <  0.5: Descend
        msg = self.vehicle.message_factory.set_attitude_target_encode(
            0,  # time_boot_ms
            1,  # Target system
            1,  # Target component
            0b00000000 if use_yaw_rate else 0b00000100,
            self.to_quaternion(roll_angle, pitch_angle, yaw_angle),  # Quaternion
            0,  # Body roll rate in radian
            0,  # Body pitch rate in radian
            math.radians(yaw_rate),  # Body yaw rate in radian/second
            thrust  # Thrust
        )
        self.vehicle.send_mavlink(msg)
        print("send msg")

    def to_quaternion(self, roll=0.0, pitch=0.0, yaw=0.0):
        """
        Convert degrees to quaternions
        """
        t0 = math.cos(math.radians(yaw * 0.5))
        t1 = math.sin(math.radians(yaw * 0.5))
        t2 = math.cos(math.radians(roll * 0.5))
        t3 = math.sin(math.radians(roll * 0.5))
        t4 = math.cos(math.radians(pitch * 0.5))
        t5 = math.sin(math.radians(pitch * 0.5))

        w = t0 * t2 * t4 + t1 * t3 * t5
        x = t0 * t3 * t4 - t1 * t2 * t5
        y = t0 * t2 * t5 + t1 * t3 * t4
        z = t1 * t2 * t4 - t0 * t3 * t5

        return [w, x, y, z]

    def distance_to_current_waypoint(self,):
        """
        Gets distance in metres to the current waypoint.
        It returns None for the first waypoint (Home location).
        """
        nextwaypoint = self.vehicle.commands.next
        if nextwaypoint == 0:
            return None
        missionitem = self.vehicle.commands[nextwaypoint - 1]  # commands are zero indexed
        lat = missionitem.x
        lon = missionitem.y
        alt = missionitem.z
        targetWaypointLocation = LocationGlobalRelative(lat, lon, alt)
        distancetopoint = self.get_distance_metres(self.vehicle.location.global_frame, targetWaypointLocation)
        return distancetopoint

    def get_distance_metres(self,aLocation1, aLocation2):
        """
        Returns the ground distance in metres between two `LocationGlobal` or `LocationGlobalRelative` objects.

        This method is an approximation, and will not be accurate over large distances and close to the
        earth's poles. It comes from the ArduPilot test code:
        https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
        """
        dlat = aLocation2.lat - aLocation1.lat
        dlong = aLocation2.lon - aLocation1.lon
        return math.sqrt((dlat * dlat) + (dlong * dlong)) * 1.113195e5
    def setup_camera(self):
        """Initialize camera.
        """
        self.capture = cv2.VideoCapture(0)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()

        self.timer.timeout.connect(self.display_video_stream_threat)
        self.timer.start(30)
    def hedef_gosterme_hazirlik(self):
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.display_harita_threat)
        self.timer2.start(30)
    def kamikaze_dalis(self):
        self.timer3 = QTimer()
        self.timer3.timeout.connect(self.kamikaze_dalis_threat)
    def kamikaze_dalis_threat(self):
        if self.vehicle.commands.next == 2 :
            irtifa = self.vehicle.location.global_relative_frame.alt
            hedef_uzaklik = self.distance_to_current_waypoint()
            dalis_acisi = 50
            dalisa_baslanacak_nokta = irtifa / math.tan(dalis_acisi * math.pi / 180)
            print("dalis uzaklik :" , dalisa_baslanacak_nokta)
            print("hedef uzaklik :", hedef_uzaklik)
            if hedef_uzaklik < dalisa_baslanacak_nokta + 5 or hedef_uzaklik < dalisa_baslanacak_nokta - 5:
                self.vehicle.mode = "GUIDED"
                if self.vehicle.attitude.pitch > -30:
                    self.send_attitude_target(0,-48,0,0,False,0)


        """if self.temp < 1:
            self.att_heading_deg = math.degrees(self.vehicle.attitude.yaw) % 360
            print("att_heading", self.att_heading_deg, "target_deg", self.deg)
            self.set_ground_course(self.deg, self.alt)
            # self.set_ground_course(self.att_heading_deg+10, alt)
            if (self.deg - 6 < self.att_heading_deg < self.deg + 6):
                self.temp = 1
                print("donus bitti")
        else :
            if self.vehicle.attitude.pitch > -30:
                #self.timer3.stop()
                self.send_attitude_target(0,-45,0,thrust=0)
                print("dalisa gecti")"""


    def display_harita_threat(self):
        frame = self.hedef_harita(self.ihalar,self.lat,self.lon)
        self.iha_lat , self.iha_lon = self.iha_koordinat_al()
        """frame2 = self.kamikaze_harita(self.iha_lat,self.iha_lon)
        if self.harita == 0:
            frame = frame
        else : frame = frame2"""
        frame = cv2.resize(frame,(700,550))
        image = QImage(frame, frame.shape[1], frame.shape[0],
                       frame.strides[0], QImage.Format_RGB888)
        self.goruntu_2.setPixmap(QPixmap.fromImage(image))
    def display_video_stream_threat(self):
        """Read frame from camera and repaint QLabel widget.
        """
        self.iha_lat, self.iha_lon = self.iha_koordinat_al()
        self.lat[0] = self.iha_lat
        self.lon[0] = self.iha_lon
        #frame = self.haberlesme.goruntu_al()
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

    """def kamikaze_harita(self,lat,lon):
        # yarisma zamani kamikaze noktalari alindigi zaman buraya array olarak koordinatlari eklenecek
        hedef_lat = [lat, 40.231331]
        hedef_lon = [lon, 29.007768]
        #kamikaze_latlar = [lat,40.230618,40.232674,40.232766]
        #kamikaze_lonlar = [lon,29.006524,29.006567,29.008873]
        sayi = len(hedef_lat)

        image = cv2.imread('700x550.png')
        cv2.putText(image, "KAMIKAZE HEDEFLER", (290, 30), 1, 1, (0, 0, 0), 2)
        cv2.rectangle(image, (100, 100), (600, 450), (255, 0, 0), 1)

        for i in range (sayi):
            kamikaze_x,kamikaze_y = self.lat_lon_to_pixel(hedef_lat[i],hedef_lon[i])
            #print(self.hedef_lat[i],self.hedef_lon[i])
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
        return image"""

    def hedef_harita(self,ihalar, lat, lon):
        sayi = len(ihalar)
        image = cv2.imread('700x550.png')
        cv2.putText(image, "HEDEF IHALAR VE KAMIKAZE NOKTASI", (220, 30), 1, 1, (0, 0, 0), 2)
        cv2.rectangle(image, (100, 100), (600, 450), (0, 0, 0), 1)
        #TODO : BURDAKI HESAPLARDA BIR YANLISLIK VAR BURAYA BAK
        for i in range(sayi):
            x, y = self.lat_lon_to_pixel(lat[i], lon[i])

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
                cv2.putText(image, "ACE", (x - 20, y - 5), 1, 1, (0, 255, 0), 1)
            elif i ==1:
                cv2.circle(image, center, 2, (0, 0, 255), 2, cv2.LINE_8, 0)
                cv2.putText(image, "KMKZ", (x - 22, y - 5), 1, 1, (0, 0, 255), 1)
            else:
                cv2.circle(image, center, 2, (255, 0, 0), 2, cv2.LINE_8, 0)
                cv2.putText(image, "D" + str(ihalar[i]), (x - 10, y - 5), 1, 1, (255, 0, 0), 1)
        image = cv2.resize(image,(640,480))
        return image

    def lat_lon_to_pixel(self, lat, lon):
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
    #--------------------------------KAMIKAZE DONUS ISLEMLERI--------------------------------#
    def turn_heading(self, rot, count, alt):
        heading = math.degrees(self.vehicle.attitude.yaw) % 360

        print("heading:", heading)

        if (rot == "r"):
            deg = round(heading + count, 0)
            self.change_heading(deg, alt)
        else:
            deg = round(heading - count, 0)
            self.change_heading(deg, alt)

    def change_heading(self, deg, alt):
        self.deg = deg
        self.alt = alt
        if (self.deg > 360):
            self.deg = 360 - self.deg
        if (self.deg < 0):
            self.deg = 360 - self.deg
        self.donus_sayaci = 1


    def get_target_from_bearing(self, original_location, ang, dist, altitude=None):
        """ Create a TGT request packet located at a bearing and distance from the original point

        Inputs:
            ang     - [rad] Angle respect to North (clockwise)
            dist    - [m]   Distance from the actual location
            altitude- [m]
        Returns:
            location - Dronekit compatible
        """

        if altitude is None: altitude = original_location.alt

        # print '---------------------- simulate_target_packet'
        dNorth = dist * math.cos(ang)
        dEast = dist * math.sin(ang)
        # print "Based on the actual heading of %.0f, the relative target's coordinates are %.1f m North, %.1f m East" % (math.degrees(ang), dNorth, dEast)

        # -- Get the Lat and Lon
        tgt = self._get_location_metres(original_location, dNorth, dEast)

        tgt.alt = altitude
        # print "Obtained the following target", tgt.lat, tgt.lon, tgt.alt

        return tgt

    def _get_location_metres(self, original_location, dNorth, dEast, is_global=False):
        """
        Returns a Location object containing the latitude/longitude `dNorth` and `dEast` metres from the
        specified `original_location`. The returned Location has the same `alt and `is_relative` values
        as `original_location`.
        The function is useful when you want to move the vehicle around specifying locations relative to
        the current vehicle position.
        The algorithm is relatively accurate over small distances (10m within 1km) except close to the poles.
        For more information see:
        http://gis.stackexchange.com/questions/2951/algorithm-for-offsetting-a-latitude-longitude-by-some-amount-of-meters
        """
        earth_radius = 6378137.0  # Radius of "spherical" earth
        # Coordinate offsets in radians
        dLat = dNorth / earth_radius
        dLon = dEast / (earth_radius * math.cos(math.pi * original_location.lat / 180))

        # New position in decimal degrees
        newlat = original_location.lat + (dLat * 180 / math.pi)
        newlon = original_location.lon + (dLon * 180 / math.pi)

        if is_global:
            return LocationGlobal(newlat, newlon, original_location.alt)
        else:
            return LocationGlobalRelative(newlat, newlon, original_location.alt)

    def ground_course_2_location(self, angle_deg, altitude=None):
        """ Creates a target to aim to in order to follow the ground course
        Input:
            angle_deg   - target ground course
            altitude    - target altitude (default the current)

        """
        tgt = self.get_target_from_bearing(original_location=self.location_current,
                                           ang=math.radians(angle_deg),
                                           dist=5000,
                                           altitude=altitude)
        # print("tgt:",tgt)
        return (tgt)

    def goto(self, location):
        """ Go to a location

        Input:
            location    - LocationGlobal or LocationGlobalRelative object

        """
        self.vehicle.simple_goto(location)

    def set_ground_course(self, angle_deg, altitude=None):
        """ Set a ground course

        Input:
            angle_deg   - [deg] target heading
            altitude    - [m]   target altitude (default the current)

        """

        # -- command the angles directly
        self.goto(self.ground_course_2_location(angle_deg, altitude))
    # --------------------------------KAMIKAZE DONUS ISLEMLERI--------------------------------#
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())