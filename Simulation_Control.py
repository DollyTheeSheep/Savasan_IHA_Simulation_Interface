import threading
import pygame

class controller():
    controller = None
    axis_data = None
    def controller_init(self):
        pygame.init()
        pygame.joystick.init()
        self.controller=pygame.joystick.Joystick(0)
        self.controller.init()
        if not self.axis_data:
            self.axis_data = {}
    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                self.axis_data[event.axis] = round(event.value, 2)
                for i in len(self.axis_data):
                    print(self.axis_data[i])

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

    def run(self):
        while not self.stopped.wait(0.1):
            #/------------------------------------------------------- 10 Hz ile yapilmasi gereken islemleri buranin altina yaz -------------------------------------------------------\#
            kumanda.listen()
            print("10 HZ")

if __name__ == '__main__':
    stopFlag = threading.Event()

    thread_5HZ = HZ5(stopFlag)
    thread_10HZ = HZ10(stopFlag)
    #/------------------------------------------------------- Kumandayı Oluştur -------------------------------------------------------\#
    kumanda = controller()
    kumanda.controller_init()

    #/------------------------------------------------------- Sayaçları Başlat -------------------------------------------------------\#
    #thread_5HZ.start()
    #thread_10HZ.start()

