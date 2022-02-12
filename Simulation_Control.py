import threading
import pygame
import pygame,time
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import time
from pymavlink import mavutil

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
                    self.axis0=2200-self.custom_map(round(event.value,2),1,-1,0,1100)
                if (event.axis == 1):
                    self.axis1=1100+self.custom_map(round(event.value,2),1,-1,0,1100)
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

    def run(self):
        while not self.stopped.wait(0.2):
            #/------------------------------------------------------- 5 Hz ile yapilmasi gereken islemleri buranin altina yaz -------------------------------------------------------\#

            print("5 HZ")

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
    #thread_5HZ.start()
    thread_10HZ.start()






