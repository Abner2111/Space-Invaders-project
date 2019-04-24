import pygame
import sys
import random
from Clases import*
from pygame import ftfont
pygame.init()
pygame.font.init()
def proceso(jugador,fps,frames_totales,sonido_jugador,sonido_enemigo):
    if isinstance(player,int) and isinstance (fps,int) and isinstance(frames_totales, int) and isinstance (sonido_jugador,int) and isinstance(sonido_enemigo,int):
        return self.proceso_aux(jugador,fps,frames_totales,sonido_jugador,sonido_enemigo,0)
    else:return "Error"
    spawn(fps,frames_totales)
    colision()
    disparo_enemigo(fps,frames_totales,sonido_enemigo)
    deconstruct(fps,frames_totales)
    keys=pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.velx=5
    elif keys[pygame.K_a]:
        player.velx=-5
    elif keys[pygame.K_w]:
        player.vely=-5
    elif keys[pygame.K_s]:
        player.vely=5
    elif keys[pygame.K_SPACE]:
        proyectil_jugador(jugador.rect.centerx,jugador.rect.centery,2,10,"../pics/laser.jpg")
        sonido_jugador.play()
    else: player.velx=0

def proceso_aux(jugador,fps,frames_totales,sonido_jugador,sonido_enemigo,event):
    if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()

def disparo_enemigo(fps,frames_totales,sonido_enemigo):
    frames_en_cinco_secgundos= fps*5
    if frames_totales%frame_en_cinco_segundos==0:
        disparo.enemigo()
        sonido_enemigo.play()

def spawn(fps,frames_totales):
    frames_en_cuatro_segundos=fps*4
    if frames_totales%frames_en_cuatro_segundos==0:
        r=random.randint(1,2)
        x=1
        if r==1:
            x=400
        elif r == 2:
            x=400

        nuevo_enemigo=enemigo(x,20,50,29,"../imagenes/enemigo.gif")
        if random.randint(1,2) ==2:
            nuevo_enemigo.velx= -nuevo_enemigo.velx

def desconstruir(fps,frames_totales,lista,vida):
    frames_en_tres_segundos=fps*3
    if isinstance (fps,int) and isinstance (frames_totales,int) and isinstance (lista,list) and isinstance (vida,int):
        return descontruir_aux(fps,frames_totales,lista,vida,0,0)
    else:return"Error"
    if vida.enemigo==0:
        General.allsprites.remove(enemigo)
        enemigo.lista.remove(enemigo)
        del enemigo

def desconstruir_aux(fps,frames_totales,lista,vida,resultado,indice):
    if indice==len(lista) and frames_totales%frames_en_tres_segundos==0:
        return resultado
    elif isinstance (lista[indice],list):
        return descontruir_aux(fps,frames_totales,lista[indice],vida,0,0)+descontruir_aux(fps,frames_totales,lista,vida,resultado,indice+1)
    else: return descontruir_aux(fps,frames_totales,lista,vida,resultado+lista[indice],indice+1)


def colision():
    for enemigo in enemigo.lista:
        golpe_enemigo=pygame.sprite.spritecollide(enemigo,proyectil_jugador.lista,True)
        if len(golpe_enemigo)>0:
            if enemigo.vida !=0:
                enemigo.vida -= enemigo.daño_recibido


    for jugador in jugador.lista:
        golpe_jugador= pygame.sprite.spritecollide(juagor,proyectil_enemigo.lista,True)
        if len(golpe_jugador)>0:
            if jugador.vida!=0: jugaodr.vida -= jugador.daño_recibido

    for jugador in jugador.lista:
        golpe_jugador = pygame.spritecollide(jugador,enemigo.lista,False)
        if len(golpe_jugador)!=0:
            jugador.vida=0

screen_size = [1280, 720] #variable que contiene dimensiones de pantalla

win = pygame.display.set_mode((screen_size[0],screen_size[1])) #surface principal

pygame.display.set_caption("Space Invaders: by Noel and Abner")

font = pygame_font.Font(None, 20)
font.render_to(win, (255, 237), "Space Invaders", pygame.Color("White"), size=48)

