import cv2
import image
import deposit
import robotMove

ser = robotMove.init("/dev/tty.usbmodem1411")

#while rval:

while(True):

    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        print("its opened")
        rval, frame = vc.read()
    else:
        rval = False

    cv2.imshow("preview", frame)
    cv2.imwrite('pics/0.jpg', frame)

    cv2.destroyWindow("preview")
    vc.release()

    count = 0

    is_coin = image.check_coin("pics/0.jpg")

    if is_coin:
      robotMove.moveForward(ser)
      print("There's a coin!")
      deposit.found_coin()
      robotMove.playMusic(ser)
      count = 0
    else:
      robotMove.turnLeft(ser)
      count+=1
      if count == 4:
        robotMove.moveForward(ser)
        robotMove.moveForward(ser)
        count = 0
