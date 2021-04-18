import pygame
import os
import random
from spaceship import Nave 
from meteoro import Meteoro
from explosion import Explosion
from itens import heart

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comicsans',40)

#VARIÁVEIS
width = 900
height = 600
score = 0
i = 0
k = 0
z = 0
tiros = []
px_fundo = 0
run = True
somStatus = False
current_time = 0
timeMeteoro = 0
criarMeteoroTempo = 0
timeFoguete = 0
count_meteoro = []
count_explosions = []
som_fundo = pygame.mixer.Sound(os.path.join('som','fundo.mp3'))

#criando um canvas
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Meteoro')
img_fundo = pygame.image.load(os.path.join('fundo','fundo.png'))
clock = pygame.time.Clock()  
#nave    
ship = Nave(0,height/2,win,width,height)
coracao = heart(300,300,win)

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

    #coracao 
    coracao.draw_heart()
    
    #desenhando o tiro
    for bala in tiros:
        bala.draw_bullet(win,k)
        bala.rectBullets.x += 8
        bala.remover_balas(False)

    #desenhando o meteoro
    meteoro_img_control()
    global score
    for meteoro in count_meteoro:
        meteoro.mov_meteoro(count_meteoro)
        meteoro.desenhar_meteoro(win)
   
    #desenhando explosões
    for explosion in count_explosions:
        explosion.explosion_timer(current_time)

    #desenhando texto
    points_text = font.render('Pontuação: '+str(score),1,(255,255,255))
    health_text = font.render('Health: '+str(ship.health),1,(255,255,255))
    win.blit(points_text,(0,0))
    win.blit(health_text,(230,0))

def collisionFunc(count_meteoro,tiros,ship):
    global score
    global run
    #check collission

    for meteoro in count_meteoro:
        #Meteoro vs Nave
        if meteoro.rect.colliderect(ship.rectNave):
            meteoro.remove_meteoro(count_meteoro,True)
            ship.nav_collision()
            explosao = Explosion(meteoro.rect.x,meteoro.rect.y,win,count_explosions)
            count_explosions.append(explosao)
            if ship.health <= 0:
                run = False
        for tiro in tiros:
            if meteoro.rect.colliderect(tiro.rectBullets):
                score +=1
                #Criando explosão
                explosao = Explosion(meteoro.rect.x,meteoro.rect.y,win,count_explosions)
                count_explosions.append(explosao)
                meteoro.remove_meteoro(count_meteoro,True)
                tiro.remover_balas(True)
        if ship.rectNave.colliderect(coracao.rect_heart):
            ship.health = coracao.health_restore(ship.health)
            print('colidiu com o coração')

def criar_meteoro():
    global criarMeteoroTempo
    if len(count_meteoro) < 10 and current_time - criarMeteoroTempo >= 1000:
        criarMeteoroTempo = pygame.time.get_ticks()
        meteoro = Meteoro(width+50,random.randint(0, height),random.randint(2,7))
        count_meteoro.append(meteoro)

def playMusic():
    #Musica de Fundo
    global somStatus
    if somStatus == False:
        som_fundo.play(-1)
        somStatus = True

def meteoro_img_control():
    #meteoro
    global timeMeteoro
    if current_time - timeMeteoro >= 80:
        timeMeteoro = pygame.time.get_ticks()
        for meteoro in count_meteoro:
            meteoro.mudar_img()

#Loop principal do game
while run:
    current_time = pygame.time.get_ticks()
    clock.tick(60)
    win.fill((0,0,0))
    
    #playMusic
    playMusic()

    #Criar meteoro
    criar_meteoro()

    
    #Controle Movimentação
    userInput = pygame.key.get_pressed()
    ship.control_nave(userInput,current_time,tiros)
    
    #collisionCheck
    collisionFunc(count_meteoro,tiros,ship)
    
    #encerrando o game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #desenhando
    draw()
    pygame.display.update()



