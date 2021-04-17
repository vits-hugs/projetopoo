import pygame
import os
import time

#Class Nave
class Nave:

    #Atributos
    def __init__(self,x,y,win,width,height):
        #movimentação
        self.width = width
        self.height = height
        self.velx = 10
        self.img = pygame.transform.scale(pygame.image.load(os.path.join('nave\Ship5.png')),(70,70))
        self.img2 =[
            pygame.transform.scale(pygame.image.load(os.path.join('nave\exhaust1.png')),(40,40)),
            pygame.transform.scale(pygame.image.load(os.path.join('nave\exhaust2.png')),(40,40)),
            pygame.transform.scale(pygame.image.load(os.path.join('nave\exhaust3.png')),(40,40)),
            pygame.transform.scale(pygame.image.load(os.path.join('nave\exhaust04.png')),(40,40))
        ]
        self.win = win
        self.tiros = []
        self.tempoTiro  = 0
        self.rectNave = self.img.get_rect()
        self.rectNave.x = x
        self.rectNave.y = y

    #MÉTODOS 

    #movimentação
    def control_nave(self,userInput,current_time,tiros):
        if userInput[pygame.K_d]:
            if self.rectNave.x < self.width:
                self.rectNave.x += self.velx
        if userInput[pygame.K_a]:
            if self.rectNave.x > 0:
                self.rectNave.x -=self.velx
        if userInput[pygame.K_s]:
            if self.rectNave.y < self.height:
                self.rectNave.y +=self.velx
        if userInput[pygame.K_w]:
            if self.rectNave.y > 0:
                self.rectNave.y -=self.velx
        if userInput[pygame.K_j]:
            if len(self.tiros) < 5 and (current_time - self.tempoTiro) >= 750:
                self.tempoTiro = pygame.time.get_ticks()
                bala = Bullets(self.rectNave.x,self.rectNave.y,tiros,self.width)
                tiros.append(bala)
                bala.som_tiro()
            
    #desenhando a nave
    def draw_nave(self,space_ship):
        self.win.blit(space_ship.img,(space_ship.rectNave.x,space_ship.rectNave.y))

    #desenhando a turbina
    def draw_turbina(self,i,space_ship):
        self.win.blit(space_ship.img2[i],(self.rectNave.x-27,self.rectNave.y+21))
    def draw_tiro(self,k,space_ship):
        self.win.blit(space_ship.imgtiro[k],(100,100))
   

class Bullets:
    def __init__(self,x,y,tiros,width):
        self.imgtiro = pygame.transform.scale(pygame.image.load(os.path.join('shot5\shot5_5.png')),(100,100))
        self.shoot_sound = pygame.mixer.Sound(os.path.join('som\shoot_sound.mp3'))
        self.rectBullets = pygame.Rect(x,y,50,50)
        self.rectBullets.x = x
        self.rectBullets.y = y
        self.tiros = tiros
        self.width = width

    def draw_bullet(self,win,k):
        win.blit(self.imgtiro,(self.rectBullets.x+15,self.rectBullets.y-15))
    
    def som_tiro(self):
        self.shoot_sound.play()

    def remover_balas(self,value):
        if value == True:
            self.tiros.remove(self)
        if len(self.tiros) > 0 and self.tiros[0].rectBullets.x > self.width:
            self.tiros.remove(self.tiros[0])

        
    
