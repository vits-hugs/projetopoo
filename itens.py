import pygame
import os
import random
class heart:
    def __init__(self,win,width,height):
        self.heart_img = pygame.transform.scale(pygame.image.load(os.path.join('itens','heart.png')),(100,100))
        self.width = width
        self.py = random.randint(0,height)
        self.px = self.width + 30
        self.height = height
        self.rect_heart = pygame.Rect(self.px,self.py,70,70)
        self.rect_heart.x = self.px
        self.rect_heart.y = self.py
        self.win = win
        self.heart_vel = 7
    def health_restore(self,ship_health):
        ship_health +=1 
        return ship_health
    def draw_heart(self):
        self.win.blit(self.heart_img,(self.rect_heart.x,self.rect_heart.y))

    def move_heart(self,coracao_array_object):
        self.rect_heart.x -= self.heart_vel
        if self.rect_heart.x <= - (self.width + 70):
            coracao_array_object.remove(self)
    



