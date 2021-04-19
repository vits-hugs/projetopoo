import pygame
import os
class Meteoro:
    def __init__(self,px,py):
        self.meteoro_img1 = [
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10000.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10001.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10002.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10003.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10004.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10005.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10006.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10007.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10008.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10009.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10010.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10011.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10012.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10013.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10014.png')),(70,70)),
            pygame.transform.scale(pygame.image.load(os.path.join('meteoro','a10015.png')),(70,70))
            ]
        self.vel = 8
        self.py = py
        self.px = px
        self.z = len(self.meteoro_img1)-1
        self.rect = pygame.Rect(px,py,10,35)
        self.rect.x = px
        self.rect.y = py
        self.exptimer = 0
    #método
    def desenhar_meteoro(self,win):
        win.blit(self.meteoro_img1[self.z],(self.rect.x,self.rect.y))
    def mudar_img(self):
        if self.z == 0:
            self.z = len(self.meteoro_img1)-1
        else:
            self.z -=1
    def mov_meteoro(self,count_meteoro):
        self.rect.x -= self.vel 
        if self.rect.x <= -35:
            self.remove_meteoro(count_meteoro,False)

    def remove_meteoro(self,count_meteoro,value):
        count_meteoro.remove(self)
     


        

            




        





    








