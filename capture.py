#!/usr/bin/env python2

import time

import pygame
import pygame.camera
from pygame.locals import *


def main():
    pygame.init()
    pygame.camera.init()

    capture_all()

def capture_all():
    camlist = pygame.camera.list_cameras()
    for i, c in enumerate(camlist):
        print "Trying camera {} from {}:".format(i, c)
        cam = pygame.camera.Camera(c, (10000,10000))
        cam.start()

        print "Camera size:", cam.get_size()
        image = cam.get_image()
        cam.stop()

        file_name = "cam.{}.{}.png".format(i, int(time.time()))
        pygame.image.save(image, file_name)
        print "Image saved:", file_name 

main()
