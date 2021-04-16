import pygame
import os
import time
import random
from spaceship import Nave 
from meteoro import Meteoro
from explosion import Explosion

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comicsans',40)

#VARIÁVEIS
width = 900
height = 600
i = 0
k = 0
z = 0
tiros = []
y = 300
x = 300
px_fundo = 0
radius = 20
vel = 10
run = True
som_fundo = pygame.mixer.Sound('som\\fundo.mp3')
somStatus = False
current_time = 0
timeMeteoro = 0
criarMeteoroTempo = 0
timeFoguete = 0
score = 0
count_meteoro = []
count_explosions = []

#criando um canvas
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Meteoro')
img_fundo = pygame.image.load('fundo\\fundo.png').convert()


clock = pygame.time.Clock()      
ship = Nave(0,height/2,win,width,height)

def draw():
    #Movimentação do fundo
    global px_fundo
    if px_fundo == -(width):
        px_fundo = 0
    win.blit(img_fundo,(px_fundo,0))
    win.blit(img_fundo,(width+px_fundo,0))
    px_fundo -=2

    #desenhando turbina
    global i
    if i >= 3:
        ship.draw_turbina(i,ship)
        i = 0
    else:
        ship.draw_turbina(i,ship)
        global timeFoguete 
        if current_time - timeFoguete >= 75:
            i +=1
            timeFoguete = pygame.time.get_ticks()
    
    #desenhando a nave
    ship.draw_nave(ship)
    
    #desenhando o tiro
    for bala in tiros:
        bala.draw_bullet(win,k)
        bala.rectBullets.x += 8
        bala.remover_balas(False)

    #desenhando o meteoro
    global score
    for meteoro in count_meteoro:
        meteoro.mov_meteoro(count_meteoro)
        meteoro.desenhar_meteoro(win)
        #Checando colisão
        if meteoro.rect.colliderect(ship.rectNave) == True:
            meteoro.remove_meteoro(count_meteoro,True)
        for balas in tiros:
            if meteoro.rect.colliderect(balas.rectBullets):
                score +=1
                #Criando explosão
                explosao = Explosion(meteoro.rect.x,meteoro.rect.y,win,count_explosions)
                count_explosions.append(explosao)
                
                meteoro.remove_meteoro(count_meteoro,True)
                balas.remover_balas(True)
   
    #desenhando explosões
    for explosion in count_explosions:
        explosion.explosion_timer(current_time)




                

                
    #desenhando fonts
    texto = font.render('Pontuação: '+str(score),1,(255,255,255))
    win.blit(texto,(0,0))

def criar_meteoro():
    global criarMeteoroTempo
    if len(count_meteoro) < 10 and current_time - criarMeteoroTempo >= 1000:
        criarMeteoroTempo = pygame.time.get_ticks()
        meteoro = Meteoro(width+50,random.randint(0, height),random.randint(2,7))

        count_meteoro.append(meteoro)



#Loop principal do game
while run:
    current_time = pygame.time.get_ticks()
    clock.tick(60)
    win.fill((0,0,0))

    #Musica de Fundo
    if somStatus == False:
        som_fundo.play(-1)
        somStatus = True
    #Criar meteoro
    criar_meteoro()

    
    #Controle Movimentação
    userInput = pygame.key.get_pressed()
    ship.control_nave(userInput,current_time,tiros)
    if userInput[pygame.K_k]:
        contador2 = pygame.time.get_ticks()
    
    #Controle do tempo
    if current_time - timeMeteoro >= 80:
        timeMeteoro = pygame.time.get_ticks()
        for meteoro in count_meteoro:
            meteoro.mudar_img()
    
    #encerrando o game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    draw()
    pygame.display.update()



