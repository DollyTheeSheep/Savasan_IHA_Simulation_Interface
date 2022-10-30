import rospy
import cv2, imutils, socket
import numpy as np
import time
import base64
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class goruntu:
    def __init__(self):
        self.BUFF_SIZE = 65536
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.BUFF_SIZE)
        self.host_name = socket.gethostname()
        self.host_ip = '192.168.1.20'  # socket.gethostbyname(host_name)
        print(self.host_ip)
        self.port = 9999
        self.socket_address = (self.host_ip, self.port)
        self.server_socket.bind(self.socket_address)
        self.WIDTH = 400
        self.fps, self.st, self.frames_to_count, self.cnt = (0, 0, 20, 0)
        self.msg, self.client_addr = self.server_socket.recvfrom(self.BUFF_SIZE)
        print('GOT connection from ', self.client_addr)
    def goruntu_aktar(self, data):
        self.frame = imutils.resize(data, width=self.WIDTH)
        self.encoded, self.buffer = cv2.imencode('.jpg', self.frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        self.message = base64.b64encode(self.buffer)
        self.server_socket.sendto(self.message, self.client_addr)
        self.frame = cv2.putText(self.frame, 'FPS: ' + str(self.fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow('TRANSMITTING VIDEO', self.frame)
        self.key = cv2.waitKey(1) & 0xFF
        if self.key == ord('q'):
            self.server_socket.close()
        if self.cnt == self.frames_to_count:
            try:
                self.fps = round(self.frames_to_count / (time.time() - self.st))
                self.st = time.time()
                self.cnt = 0
            except:
                pass
        self.cnt += 1
class camera_1:
    def __init__(self):
        #/--------------------------------------- ROS ---------------------------------------\#
        self.image_sub = rospy.Subscriber("/ZephyrPlane/boreas/camera/image_raw", Image, self.callback)
        #/--------------------------------------- Socket ---------------------------------------\#
        self.a=0


    def callback(self, data):
        #/--------------------------------------- Ros ---------------------------------------\#
        bridge = CvBridge()
        try:
            cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)

        image = cv_image
        frame = cv2.resize(image, (400, 400))
        #cv2.imshow("Camera output normal", self.frame)
        # /--------------------------------------- Socket ---------------------------------------\#
        if self.a == 0:
            self.video = goruntu()
            print("goruntu nesnesi olustu")
            self.a=1
        self.video.goruntu_aktar(frame)


def main():
    camera_1()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo("Shutting down")

    cv2.destroyAllWindows()


if __name__ == '__main__':
    rospy.init_node('camera_read', anonymous=False)
    main()