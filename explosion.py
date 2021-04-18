import pygame

class Explosion:
    def __init__(self,mpx,mpy,win,count_explosions):
        self.explosion_img = [pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_1.png'),(70,70)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_2.png'),(130,130)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_3.png'),(130,130)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_4.png'),(130,130)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_5.png'),(130,130)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_6.png'),(130,130)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_7.png'),(130,130)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_8.png'),(130,130)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_9.png'),(130,130)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_10.png'),(130,130)),pygame.transform.scale(pygame.image.load('Explosion3\\Explosion2_11.png'),(130,130))]
        self.explosionTimer = 0
        self.explosion_count = 0
        self.meteor_px = mpx-20
        self.meteor_py = mpy-30
        self.win = win
        self.count_explosions = count_explosions

    def explosion_timer(self,current_time):
        if (current_time - self.explosionTimer) >= 100:
            self.explosionTimer = pygame.time.get_ticks()
            self.explosion_meteor_bullet()

    def explosion_meteor_bullet(self):
        self.win.blit(self.explosion_img[self.explosion_count],(self.meteor_px,self.meteor_py))
        
        if self.explosion_count >=10:
            self.count_explosions.remove(self)            
        else:
            self.explosion_count +=1
    



