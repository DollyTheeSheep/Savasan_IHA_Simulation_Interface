"""import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        l = QVBoxLayout()
        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(self.toggle_window1)
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(self.toggle_window2)
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window1(self, checked):
        if self.window1.isVisible():
            self.window1.hide()

        else:
            self.window1.show()

    def toggle_window2(self, checked):
        if self.window2.isVisible():
            self.window2.hide()

        else:
            self.window2.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()"""
import time

import cv2
def lat_lon_to_pixel(lat,lon):
    harita_piksel_x, harita_piksel_y = 500,350
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

    sonuc_piksel_x = sonuc_lon/lonlar_fark*500
    sonuc_piksel_y = sonuc_lat/latlar_fark * 350
    print("deneme" + str(sonuc_piksel_x), str(sonuc_piksel_y))
    return int(sonuc_piksel_x),int(sonuc_piksel_y)

def kamikaze_harita(ACE,lat,lon):

    # yarisma zamani kamikaze noktalari alindigi zaman buraya array olarak koordinatlari eklenecek
    kamikaze_xler = []
    kamikaze_yler = []
def hedef_harita(ihalar,lat,lon):
    sayi = len(ihalar)
    image = cv2.imread('700x550.png')
    cv2.putText(image, "HEDEF IHALAR", (290,30), 1, 1, (0, 0, 0), 2)
    cv2.rectangle(image, (100,100), (600, 450), (255, 0, 0), 1)

    for i in range(sayi):
        x,y=lat_lon_to_pixel(lat[i],lon[i])
        print(x,y)

        if x>0:x = x+100
        if y>0:y= (350-y) + 100

        if x > 700 : x = 700
        if x < 0 and x > -100 : x = x*(-1)
        if x <= -100: x = 0

        if y > 550 : y = 550
        if y < 0 and y > -100 : y = (y*(-1)) + 450
        if y < -100: y = 550

        center = (x, y)

        if i == 0:
            cv2.circle(image, center, 2,(0, 255, 0), 2,cv2.LINE_8, 0)
            cv2.putText(image, "ACE", (x - 15, y - 5), 1, 1, (0, 255, 0), 1)
        else:
            cv2.circle(image, center, 2, (0, 0, 255), 2,cv2.LINE_8, 0)
            cv2.putText(image, "D"+str(ihalar[i]), (x-10,y-5), 1, 1, (0, 0, 255), 1)

    cv2.imshow("Model Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ihalar = [5,6,7,8,9,10,11,12,13]
lat = [40.231478,40.230758,40.232183,40.231528,40.232191,40.232502,40.229656,40.233362,40.229337]
lon = [29.006931,29.008219,29.008734,29.008026,29.004861,29.010472,29.007967,29.007752,29.007972]

hedef_harita(ihalar,lat,lon)

