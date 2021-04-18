import pygame
import os
class heart:
    def __init__(self,px,py,win):
        self.heart_img = pygame.transform.scale(pygame.image.load(os.path.join('itens','heart.png')),(100,100))
        self.rect_heart = pygame.Rect(px,py,70,70)
        self.win = win
    def health_restore(self,ship_health):
        ship_health +=1 
        return ship_health
    def draw_heart(self):
        self.win.blit(self.heart_img,(self.rect_heart.x,self.rect_heart.x))
