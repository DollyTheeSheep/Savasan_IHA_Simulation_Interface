import threading


class HZ5(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.2):
            print("5 HZ")

class HZ10(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(0.1):
            print("10 HZ")

if __name__ == '__main__':
    stopFlag = threading.Event()

    thread_5HZ = HZ5(stopFlag)
    thread_10HZ = HZ10(stopFlag)

    # /------------------------------------------------------- Sayaçları Başlat -------------------------------------------------------\#
    #thread_5HZ.start()
    #thread_10HZ.start()
