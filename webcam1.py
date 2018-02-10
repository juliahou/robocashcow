import pygame
import pygame.camera
import os
from pygame.locals import *
import image
import deposit
import robotMove

pygame.init()
pygame.camera.init()
os.system("rm -rf pics")
os.system("mkdir pics")

ser = robotMove.init("/dev/tty.usbmodem1411")

camlist = pygame.camera.list_cameras()
counter = 0
if camlist:
  while True:
    cam = pygame.camera.Camera(camlist[0],(640,480))
    cam.start()
    img = cam.get_image()
    pygame.image.save(img,"pics/"+str(counter)+".jpg")
    is_coin = image.check_coin("pics/"+str(counter)+".jpg")
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
    counter += 1
