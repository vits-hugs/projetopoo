import pygame
import os
import random
from spaceship import Nave 
from meteoro import Meteoro
from explosion import Explosion
from itens import heart
from boss import Stoneman

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
bossStatus = False
boss = 0
current_time = 0
timeMeteoro = 0
criarMeteoroTempo = 0
timeFoguete = 0
count_meteoro = []
count_explosions = []
som_fundo = pygame.mixer.Sound(os.path.join('som','fundo.mp3'))
coracao_tempo = 0
coracao_array_object = []
NaveDead = False


#criando um canvas
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('Meteoro')
img_fundo = pygame.image.load(os.path.join('fundo','fundo.png'))
game_over_fundo = pygame.image.load(os.path.join('fundo','screen.png'))
clock = pygame.time.Clock()  
#nave    
ship = Nave(0,height/2,win,width,height)


def draw():
    #Movimentação do fundo
    global px_fundo
    global bossStatus 
    global boss
    global i
    global timeFoguete 

    if px_fundo == -(width):
        px_fundo = 0
    win.blit(img_fundo,(px_fundo,0))
    win.blit(img_fundo,(width+px_fundo,0))
    px_fundo -=2

    #desenhando turbina
    if i >= 3:
        ship.draw_turbina(i,ship)
        i = 0
    else:
        ship.draw_turbina(i,ship)
        if current_time - timeFoguete >= 75:
            i +=1
            timeFoguete = pygame.time.get_ticks()
    
    #desenhando a nave
    ship.draw_nave(ship)

    #coracao 
    global coracao_array_object
    for coracao in coracao_array_object:
        # Move e Remove coracao
        coracao.move_heart(coracao_array_object)
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

    #desenhando o boss
    
    if score >= 0 and bossStatus == False:
        bossStatus = True
        boss = Stoneman(width,height,win)
    if bossStatus == True:
        boss.draw_stoneman(current_time)
    
    #FUNÇÃO DE COLISÃO 
def collisionFunc(count_meteoro,tiros,ship,coracao_array_object):
    global score
    global run
    global NaveDead
    #check collission

    for meteoro in count_meteoro:
        #Meteoro vs Nave
        if meteoro.rect.colliderect(ship.rectNave):
            meteoro.remove_meteoro(count_meteoro,True)
            ship.nav_collision()
            explosao = Explosion(meteoro.rect.x,meteoro.rect.y,win,count_explosions)
            count_explosions.append(explosao)
            if ship.health <= 0:
                NaveDead = True
       
        for tiro in tiros:
             #Tiro vs Meteoro
            if meteoro.rect.colliderect(tiro.rectBullets):
                score +=1
                #Criando explosão
                explosao = Explosion(meteoro.rect.x,meteoro.rect.y,win,count_explosions)
                count_explosions.append(explosao)
                meteoro.remove_meteoro(count_meteoro,True)
                tiro.remover_balas(True)
            #Tiro vs Boss
            if boss != 0:
                if boss.stoneman_rect.colliderect(tiro.rectBullets):
                    boss.boss_decrease_health()
                    explosao = Explosion(tiro.rectBullets.x,tiro.rectBullets.y,win,count_explosions)
                    count_explosions.append(explosao)
                    tiro.remover_balas(True)
                    print('COLIDIU COM O BOSS')
            
        #Nave vs Coração
        for coracao in coracao_array_object:
            if ship.rectNave.colliderect(coracao.rect_heart):
                ship.health = coracao.health_restore(ship.health)
                coracao_array_object.remove(coracao)
        
        
        #Nave vs Tiro do Boss
        if boss != 0:
            for boss_bullet in  boss.bullet_array:
                if ship.rectNave.colliderect(boss_bullet.bullet_rect):
                    boss.bullet_array.remove(boss_bullet)
                    ship.nav_collision()
                    if ship.health <= 0:
                        NaveDead = True


def criar_meteoro():
    global criarMeteoroTempo
    if len(count_meteoro) < 15 and current_time - criarMeteoroTempo >= 500:
        criarMeteoroTempo = pygame.time.get_ticks()
        meteoro = Meteoro(width+50,random.randint(0, height))
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

def criarCoracao():
    global coracao_tempo
    global coracao_array_object
    global win
    if (current_time - coracao_tempo) >= 15000:
        coracao_tempo = pygame.time.get_ticks()
        coracao_array_object.append(heart(win,width,height))



#Loop principal do game
while run:
    if NaveDead  == False:
        print(bossStatus)
        current_time = pygame.time.get_ticks()
        clock.tick(60)
        win.fill((0,0,0))
        
        #playMusic
        playMusic()

        #Criar meteoro
        criar_meteoro()
        
        #Criar coracao
        criarCoracao()

        
        #Controle Movimentação
        userInput = pygame.key.get_pressed()
        ship.control_nave(userInput,current_time,tiros)
        
        #collisionCheck
        collisionFunc(count_meteoro,tiros,ship,coracao_array_object)
        #desenhando
        draw()
        pygame.display.update()
    else:
        win.blit(game_over_fundo,(0,0))
        print(NaveDead)
        pygame.display.update()

    #encerrando o game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



