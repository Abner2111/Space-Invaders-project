##Clases
import pygame
##clase principal a usar
class General(pygame.sprite.Sprite):

    allsprites= pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):
        pygame.sprite.Sprite.__init__(self)
        General.allsprites.add(self)
##definicion de los objetos y posiciones
        self.image= pygame.image.load(image_string)
        self.rect= self.image,get_rect()

        self.width=width
        self.height=height
        self.rect.centerx=x
        self.rect.centery=y
    def draw(self,surface):
        surface.blit(self.image,(self.rect.x-self.rect.width/2,self.rect.y-self.rect.height))

    def destroy(self,ClassName):
        ClassName.List.remove(self)
        General.allsprites.remove(self)
        del self

##clases de objetos
class Naves(General):
    lista= pygame.sprite.Group
    score=0
    def __init__(self,x,y,width,height,image_string):
        General. __init__(self,x,y,width,height,image_string)
        Naves.lista.add(self)
        self.health=150
        self.velx=0

    def draw(self,surface):
        surface.blit(self.image,(self.rect.x-self.rect.width/2,self.rect.y-self.rect.height))

    def move(self,width):
        self.rect.x += self.velx

####Clase de nave del jugador
class jugador(Naves):
    lista= pygame.sprite.Group()
    lista_disparos=[]
    def __init__(self,x,y,width,height,image_string):
        jugador.lista.add(self)
        self.daño_recibido=50
    def movimiento(self,SCREENWIDTH):
        if self.rect.centerx >570 and self.velx >0:
            self.velx=0
        elif self.rect.centerx <20 +(self.width) and self.velx <0:
            self.velx=0
            self.rect.x += self.velx


        @staticmethod
        def revisar_vida():
            for nave in jugador.lista:
                if nave.vida==0
                print("Game over")
                return False
            else:
                return True

####Nave enemigas

class enemigo(Naves):
    lista=pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):
        Naves.__init__(self,x,y,height,image_string)
        enemigo.lista.add(self)
        self.dead=False
        self.velx=3
        self.damagetaken=50

    def movimiento(self,SCREENWIDTH):
        if self.rect.centerx > SCREENWIDTH - (self.width) -20 or self.rect.centerx <20 +(self.width):
            self.velx= -self.velx
            self.rect.centery +=50
            self.rect.x += self.velx

    @staticmethod
    def disparo():
        for enemigos in enemigo.list:
            if enemigos.health!=0:
                disparo_enemigo(enemy.rect.centerx,enemy.rect.centery,2,10,"../imagenes/disparo_enemigo.jpg")##cambiar direccion y nombre


    @staticmethod
    def revisar_vida():
        for enemigos in enemigo.lista:
            if enemigos.health==0:
                if enemu.dead==False:
                    Naves.score+=5
                    enemy.image=pygame.image.load("../imagenes/explosiones.gif")
                    enemy.velx=0
                    enemy.dead=True

##Clase disparo
                                
                                
