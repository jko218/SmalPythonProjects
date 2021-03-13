import pygame
import random
from config import * 
class GravetyObject:
    def __init__(self, x, y, speed_x, speed_y, mass, r, move):
        self.pos = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2(speed_x, speed_y)
        #self.gravity = gravety
        self.mass = mass
        self.r = r
        self.move = move
    def Draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, self.r)
    def __force__(self, object):
        mass = self.mass * object.mass
        distance = self.pos.distance_to(object.poss) ** 2
        force =  mass/distance
        return force
    def __acseleration__(self, force):
        acseleration = force / self.mass
        return acseleration
    def __speed_change__(self, acseleration):
        pass
    def move(self, object_list, realtime):
        
        pass