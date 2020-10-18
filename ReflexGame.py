#initialising pygame

import pygame
import sys
import time
from utils import *
pygame.init()

screen = pygame.display.set_mode((width,height))

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    grid_width = pow(blockSize,2)
    centering = (width - grid_width)//2
    for x in range(20):
        for y in range(20):
            rect = pygame.Rect(x*blockSize + centering, y*blockSize + (centering-40),blockSize, blockSize)
            pygame.draw.rect(screen,WHITE,rect, 1)
            
def main():
    #initialising display 

    background = GRAY
    screen.fill(background)
    # pygame.display.update()

    #creating event loop
    running = True
    while running:
        drawGrid()
        for event in pygame.event.get():
            # print(event)
            if(event.type == pygame.QUIT):
                # screen.fill(RED)
                # pygame.display.update()
                # time.sleep(1)
                running = False
        pygame.display.update()
    pygame.quit()
    quit()

main()
