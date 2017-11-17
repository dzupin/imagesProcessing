import os
import imageio

png_dir = "./saves/png/"
images = []
for subdir, dirs, files in os.walk(png_dir):
    for file in files:
        file_path = os.path.join(subdir, file)
        if file_path.endswith(".png"):
            images.append(imageio.imread(file_path))
imageio.mimsave('./saves/gif/movie.gif', images)


import sys
import os
sys.path.append(os.path.abspath('..'))
import pygame
from pygame.locals import *
import time
import pyganim

pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption('Pyganim GIF Demo')

# create the animation objects   ('filename of image',    duration_in_seconds)
bananaAnim = pyganim.PygAnimation('./saves/gif/movie.gif')
bananaAnim.play() # there is also a pause() and stop() method

mainClock = pygame.time.Clock()
BGCOLOR = (100, 50, 50)
while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    bananaAnim.blit(windowSurface, (10, 10))

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.