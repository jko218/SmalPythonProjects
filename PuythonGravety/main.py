import pygame
import random
from objects import *
from config import * 

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
    background = pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_X, SCREEN_Y))
    test = {GravetyObject(SCREEN_X // 2, SCREEN_Y // 2, 0, 0, 5000, 80, False),
        GravetyObject(SCREEN_X - 80, SCREEN_Y // 2, 0, 15, 18, 20, True),
    GravetyObject(SCREEN_X // 2, 100, 20 , 0, 12, 35, True)}
    clock = pygame.time.Clock()


    while(GAMELOOP):

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                GAMELOOP = False
        clock.tick(FPS)
        
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_X, SCREEN_Y))
        for obj in test:
            obj.Move(test)
            obj.Draw(screen)
        pygame.display.update()
    
    pass