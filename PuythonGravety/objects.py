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
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def Draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.r)
    def __force__(self, object):
        mass = self.mass * object.mass
        distance = self.pos.distance_to(object.pos) ** 2
        force =  (mass * GRAVITY)/distance
        return force
    def __acseleration__(self, force):
        acseleration = force / self.mass
        return acseleration
    def __speed_change__(self, realtime):
        # axeleration_vector = 
        # self.speed = self.speed + 
        pass
    def Move(self, object_list):
        if self.move == True:
            acseleration = pygame.math.Vector2(0, 0)
            time = FPS / 1000
            for object in object_list:
                if object != self:
                    acseleration_nr = self.__acseleration__(self.__force__(object))
                    print(acseleration_nr)
                    tmp = pygame.math.Vector2(0, 0)
                    tmp = object.pos - self.pos
                    tmp.scale_to_length(acseleration_nr)                    
                    acseleration = acseleration + tmp
            self.speed = self.speed + acseleration * time
            self.pos = self.pos + (self.speed * time)
                
        pass

class Object_creater:
    def __init__(self, t):
        x,y = t
        self.mass = 0
        self.r = 0
        self.x = x
        self.y = y
    def write(self, x, y, screen):
        font = pygame.font.SysFont("arial", 10)
        string = "Mass: " + str(self.mass) + "\nRadius: " + str(self.r)
        info = font.render(string, True, (x, y, 8))
        screen.blit(info, (round(0.0313 * screen.get_width()) + 2, screen.get_height() - info.get_height()))
    def create_new_object(self, objectlist):
        object = GravetyObject(self.x, self.y, random(-60, 60), random(-60, 60), self.mass, self.r, True)
        objectlist.append(object)