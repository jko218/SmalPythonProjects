import pygame
import random
from objects import *
from config import * 

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
    background = pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_X, SCREEN_Y))
    test = GravetyObject(230, 223, 0, 0, 18, 60, False)

    while(GAMELOOP):

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                GAMELOOP = False
        
        background
        test.Draw(screen)
        pygame.display.update()
    
    pass