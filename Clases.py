from typing import Any

from pygame import * #importa todo l abiblioteca pygame

class General(pygame.sprite.Sprite):
    allsrpites = pygame.sprite.Group() #contenedor para todos los sprites

    def __init__(self, x, y, width, height, image_string):
        pygame.sprite.Sprite.__init__(self)
        General.allsprites.add(self)

        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()

        self.width = width
        self.height = height

        self.rect.centerx = x
        self.rect.centery = y

    def draw(self, surface) -> object: #"dibuja" a los objetos en pantalla
        surface.blit(slef.image, (self.rect.x-self.rect.width/2, self.rect.y-self.rect.height))
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
        Naves.__init__(self, x, y, width, hegiht, image_string)
        jugador.lista.add(self)
        self.destruido = False
    def revisar_derrotado(self):
        return self.destruido
class enemigo(Naves):
    lista=pygame.sprite.Group()
    def __init__(self, x, y, width, height, image_string): #posicion
        Naves.__init__(self, x, y, width, height, image_string)
        enemigo.lista.add(self)
        self.dead = False
        self.velx = 3
        self.dano_recibido = 50
    










