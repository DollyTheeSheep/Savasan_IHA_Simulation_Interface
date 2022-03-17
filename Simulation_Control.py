import threading
import pygame
import pygame,time
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import time
from pymavlink import mavutil
class mavlnk():
    def mavlnk_init(self):
        self.vehicle = connect("192.168.1.10:14560", wait_ready=True)
        print("mavlink baglanti")
    def mavlnk_kumanda_verilerini_gonder(self,aileron,pitch,throttle,yaw,mode):
        if mode < 1500 :
            self.vehicle.mode = "AUTO"
        else :
            self.vehicle.mode = "FBWA"
            self.vehicle.channels.overrides['1'] = aileron
            self.vehicle.channels.overrides['2'] = pitch
            self.vehicle.channels.overrides['3'] = throttle
            self.vehicle.channels.overrides['4'] = yaw

class controller():
    def controller_init(self):
        pygame.init()
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        for joy in self.joysticks:
            joy.init()
        self.axis0=0    #ROLL
        self.axis1=0    #PITCH
        self.axis2=0    #THROTTLE
        self.axis3=0    #MODE
        self.axis4=0    #BOS
        self.axis5=0    #YAW

    def custom_map(self,x,c_min,c_max,t_min,t_max):
        value = ((x-c_min)*(t_max-t_min))/((c_max-c_min)+t_min)
        return int(value)

    def kumanda_oku(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                if (event.axis == 0):
                    self.axis0=2120-self.custom_map(round(event.value,2),1,-1,0,1100)
                if (event.axis == 1):
                    self.axis1=1980-self.custom_map(round(event.value,2),1,-1,0,1100)
                if (event.axis == 2):
                    self.axis2=1100+self.custom_map(round(event.value,2),1,-1,0,1100)
                if (event.axis == 3):
                    self.axis3=1100+self.custom_map(round(event.value,2),-1,1,0,1100)
                    if(self.axis3<1000): self.axis3=1000
                    if(self.axis3 > 2000): self.axis3 = 2050
                if (event.axis == 5):
                    self.axis5 = 2100-self.custom_map(round(event.value, 2), 1, -1, 0, 1100)
            if event.type == pygame.JOYBUTTONDOWN:
                print(event.button)

        print("Axis0-ROLL:",self.axis0,"Axis1-PITCH:",self.axis1,"Axis2-THROTTLE:",self.axis2,"Axis3-MODE:",self.axis3,"Axis4:",self.axis4,"Axis5-YAW:",self.axis5)

class HZ5(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event
        # /------------------------------------------------------- Mavlink Baglantisi Yapildi -------------------------------------------------------\#
        global baglanti
        baglanti = mavlnk()
        baglanti.mavlnk_init()

    def run(self):
        while not self.stopped.wait(0.2):
            #/------------------------------------------------------- 5 Hz Ile Yapilmasi Gereken Islemleri Buranin Altina Yaz -------------------------------------------------------\#
            baglanti.mavlnk_kumanda_verilerini_gonder(kumanda.axis0,kumanda.axis1,kumanda.axis2,kumanda.axis5,kumanda.axis3)
            # Normalde 1 tane axis gonderilse 5 hz fakat 4 axis gonderildigi icin mavlink inspector da 20 hz goruluyor.
            #print("5 Hz")

class HZ10(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event
        # /------------------------------------------------------- Kumandayı Oluştur -------------------------------------------------------\#
        global kumanda
        kumanda = controller()
        kumanda.controller_init()
    def run(self):
        while not self.stopped.wait(0.1):
            #/------------------------------------------------------- 10 Hz ile yapilmasi gereken islemleri buranin altina yaz -------------------------------------------------------\#
            kumanda.kumanda_oku()


if __name__ == '__main__':
    stopFlag = threading.Event()

    thread_5HZ = HZ5(stopFlag)
    thread_10HZ = HZ10(stopFlag)

    #/------------------------------------------------------- Sayaçları Başlat -------------------------------------------------------\#
    thread_5HZ.start()
    thread_10HZ.start()






