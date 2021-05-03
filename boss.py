import pygame
import os
import random

#Nicolas

class Enemy:
    def __init__(self,width,height,win):
        self.health = 1
        self.width = width
        self.height = height
        self.boss_img_enemy =pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('enemy','boss.png')),(130,130)),-90)
        self.enemy_rect = pygame.Rect(width/2,height/2,70,70)
        self.enemy_rect.x = width/2
        self.enemy_rect.y = height/2
        self.movy = True
        self.movx = True
        self.win = win
        self.bullet_array = []
        self.attack_timer = 0
    def draw_enemy(self,current_time):
        self.move_boss(current_time)
        self.win.blit(self.boss_img_enemy,( self.enemy_rect.x, self.enemy_rect.y))

    def move_boss(self,current_time):
        #mov y
        if self.movy == True:
            self.enemy_rect.y += 1
            if self.enemy_rect.y >= self.height-100:
                self.movy = False
        if self.movy == False:
            self.enemy_rect.y -= 1
            if self.enemy_rect.y <= -(self.height - 500):
                self.movy = True

        #mov x
        if self.movx == True:    
            self.enemy_rect.x -=1
            if self.enemy_rect.x <= 500:
                self.movx = False
        if self.movx == False:
            self.enemy_rect.x +=1
            if self.enemy_rect.x >=800:
                self.movx = True
        #attack
        if (current_time - self.attack_timer) >= 1000:
            self.attack_timer = pygame.time.get_ticks()
            self.boss_attack()
        #Draw and move bullets
        for bullet in self.bullet_array:
            bullet.draw_bullet(self.win,self.bullet_array,current_time)
        

    def boss_attack(self):
        bullet = Boss_bullets(self.enemy_rect.x,self.enemy_rect.y)
        self.bullet_array.append(bullet)

    def boss_decrease_health(self):
        self.health -= 1
        




class Boss_bullets:
    def __init__(self,px,py):
        self.bullet_array_img = []
        self.bullet_rect = pygame.Rect(px,py,50,50)
        self.bullet_rect.x = px
        self.bullet_rect.y = py
        self.load_img()
        self.i = 0
        self.bullet_img_timer = 0

    def draw_bullet(self,win,bullet_array,current_time):
        if (current_time - self.bullet_img_timer) >= 50:
            self.bullet_img_timer = pygame.time.get_ticks()
            if self.i >= 59:
                self.i = 0
            else:
                self.i +=1
        win.blit(self.bullet_array_img[self.i],(self.bullet_rect.x-50,self.bullet_rect.y))

        self.move_bullet(bullet_array)
    def move_bullet(self,bullet_array):
        self.bullet_rect.x -=4
        if self.bullet_rect.x <= 0:
            bullet_array.remove(self)
    
    def load_img(self):
        for x in range(1,61):
            self.bullet_array_img.append(pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("enemy",str(x)+".png")),(70,70)),-180))

            







