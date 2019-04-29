from typing import Any
import pygame
from pygame import *  #importa todo la biblioteca pygame



class General(pygame.sprite.Sprite):#se establece la clase general
    allsprites = pygame.sprite.Group() #contenedor para todos los sprites

    def __init__(self, x, y, width, height, image_string):#se define las caracterisiticas genetrales de las clases con als que se van a trabajar 
        pygame.sprite.Sprite.__init__(self)
        General.allsprites.add(self)

        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()

        self.width = width
        self.height = height

        self.rect.centerx = x
        self.rect.centery = y

    def draw(self, surface): #"dibuja" a los objetos en pantalla
        surface.blit(self.image, (self.rect.x-self.rect.width/2, self.rect.y-self.rect.height))
    def destroy(self, ClassName): #destruye sprite
        ClassName.lista.remove(self)
        General.allsprites.remove(self)
        del self

class Naves(General): #clase general de naves
    lista = pygame.sprite.Group()
    score = 0

    def __init__(self, x, y, width, height, image_string):
        General.__init__(self, x, y, width, height, image_string)
        Naves.lista.add(self)
        self.velx = 0
        self.vely = 0
    def move(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
class Jugador(Naves):
    lista = pygame.sprite.Group()
    lista_disparos=[]

    def __init__(self, x, y, width, height, image_string):
        Naves.__init__(self, x, y, width, height, image_string)
        Jugador.lista.add(self)
        self.destruido = False
    def revisar_derrotado(self):
        return self.destruido
    def movimiento(self,SCREENWIDTH):#se define los movimientos del jugador
        if self.rect.centerx >570 and self.velx >0:#se estable que esta unicabo en el centro
            self.velx=0#y su velocidad
        elif self.rect.centerx <20 +(self.width) and self.velx <0:#se establece ubicacion y velocidad del jugador
            self.velx=0## velocidad inicial
            self.rect.x += self.velx
    
class enemigo(Naves):
    lista=pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string): #posicion
        Naves.__init__(self, x, y, width, height, image_string)
        enemigo.lista.add(self)
        self.dead = False
        self.velx = 3
        self.dano_recibido = 50
        self.formada = True
     def movimiento(self,SCREENWIDTH):# se define la posicion de los enemigos en la pantalla y los movimientos que podra realizar
        if self.rect.centerx > SCREENWIDTH - (self.width) -20 or self.rect.centerx <20 +(self.width):# es establece la ubicacion en la pantalla
            self.velx= -self.velx# se define la velocidad de las naves
            self.rect.centery +=50# se define la posicion que estaran
            self.rect.x += self.velx



class Proyectil(pygame.sprite.Sprite):
    allproy = pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.height = height
        self.rect.x = x
        self.rect.y = y
        self.vely=-8
        Proyectil.allproy.add(self)
class Proyectil_jugador(Proyectil):
    lista = pygame.sprite.Group()

    def __init__(self, x, y, width, height, image_string):
        Proyectil.__init__(self, x, y, width, height, image_string)
    def movimiento(self, x, y):
        self.rect.y+= Proyectil.vely
class Proyectil_enemigo(Proyectil):
    lista = pygame.sprite.Group()
