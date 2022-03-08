from djitellopy import Tello
import cv2
import time

from time import sleep

tello = Tello()
tello.connect()
#tello.takeoff()
print(tello.get_battery())
global img
tello.streamon()



#tello.flip_forward()
#tello.move("forward", 60)
#tello.move_forward(60)
#tello.move_left(30)
#sleep(1)
#tello.rotate_counter_clockwise(180)
#tello.land()

#tello.end()

while True:

    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("image", img)
    cv2.waitKey(1)


time.sleep(10)
cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
time.sleep(10)