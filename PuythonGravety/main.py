import pygame
import random
from objects import *
from config import * 

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y), 0, 32)
    background = pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_X, SCREEN_Y))
    test = {GravetyObject(SCREEN_X // 2, SCREEN_Y // 2, 0, 0, 50000, 40, False),
        GravetyObject(SCREEN_X - 80, SCREEN_Y // 2, 0, 15 * 3, 18, 20, True),
    GravetyObject(SCREEN_X // 2, 100, 20 * 3, 0, 12, 30, True)}
    clock = pygame.time.Clock()


    while(GAMELOOP):

        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                GAMELOOP = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == LEFTPRESS:
                    objectCreater = Object_creater(pygame.mouse.get_pos())
                    MOUSE_LEFT = True
                elif event.button == RIGHTPRESS:
                    MOUSE_RIGHT = True
                elif event.button == SCROLEUP:
                    if MOUSE_LEFT == True:
                        pass
                    pass
                elif event.button == SCROLEDOWN:
                    if MOUSE_LEFT == True:
                        pass 
                    pass
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == LEFTPRESS:
                    objectCreater.create_new_object()
                    MOUSE_LEFT = False
                
        clock.tick(FPS)
        
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_X, SCREEN_Y))
        for obj in test:
            obj.Move(test)
            obj.Draw(screen)
        pygame.display.update()
    
    pass