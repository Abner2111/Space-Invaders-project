##Clases
import pygame #####se llama las funciones de pygame 
##clase principal a usar
class General(pygame.sprite.Sprite):#Se crea una clase general para el manejo de los sprites(imagenes) que se van a usar para complementar el juego en su diseño.

    allsprites= pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):
        pygame.sprite.Sprite.__init__(self)
        General.allsprites.add(self)
##definicion de los objetos y posiciones
        self.image= pygame.image.load(image_string)
        self.rect= self.image.get_rect()

        self.width=width
        self.height=height
        self.rect.centerx=x
        self.rect.centery=y
    def draw(self,surface):
        surface.blit(self.image,(self.rect.x-self.rect.width/2, self.rect.y-self.rect.height))

    def destroy(self,ClassName):
        ClassName.List.remove(self)
        General.allsprites.remove(self)
        del self

##clases de objetos
class Naves(General): #Se crea la clase principal para las naves del jugador y de los enemigos.
    lista= pygame.sprite.Group
    score=0
    def __init__(self,x,y,width,height,image_string):
        General. __init__(self,x,y,width,height,image_string)#Caracterisiticas que se compartiran entre las naves,vida,velocidad)
        Naves.lista.add(self)
        self.health=150
        self.velx=0

    def draw(self,surface):
        surface.blit(self.image,(self.rect.x-self.rect.width/2,self.rect.y-self.rect.height))#la posicion en donde estaran y su movimiento

    def move(self,width):
        self.rect.x += self.velx #se define el movimiento hacia los lados que tendran las naves

####Clase de nave del jugador, se definiran las caracteristicas que tendra la nave del jugador.
class jugador(Naves):
    lista= pygame.sprite.Group()#se le dice que tiene caracteristica de sprite y que sus disparos(proyectiles) se encuentran en una lista
    lista_disparos=[]
    def __init__(self,x,y,width,height,image_string):#se define con que se va a trabajar 
        jugador.lista.add(self)
        self.daño_recibido=50#se define cuanto daño puede recibir el jugador
    def movimiento(self,SCREENWIDTH):#se define los movimientos del jugador
        if self.rect.centerx >570 and self.velx >0:#se estable que esta unicabo en el centro
            self.velx=0#y su velocidad
        elif self.rect.centerx <20 +(self.width) and self.velx <0:
            self.velx=0
            self.rect.x += self.velx
    def revisar_vida(self,lista,vida):
        if isinstance (lista,list) and isinstance (vida,int):
            return self.revisar_vida_aux(lista,jugador.vida,0,0)
        else: return "Error"
                
    def revisar_vida_aux(self,lista,vida,resultado,indice):
        if indice==len(lista):
            return resultado
        elif isinstance (lista[indice],list):
            return (self.revisar_vida_aux(lista[indice],vida,0,0)+self.revisar_vida_aux(lista,vida,resultado,indice+1))
        elif vida==0:
            print("Game over")
            return False
        else: return True and self.revisar_vida_aux(lista,vida,resultado+lista[indice],indice+1)
        
        


            #for jugador in jugador.lista:
              #  if jugador.vida==0:
               #     print("Game over")
                #    return False
                #else:
                 #   return True

####Nave enemigas

class enemigo(Naves):
    lista=pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):
        Naves.__init__(self,x,y,height,image_string)
        enemigo.lista.add(self)
        self.dead=False
        self.velx=3
        self.dano_recibido=50

    def movimiento(self,SCREENWIDTH):
        if self.rect.centerx > SCREENWIDTH - (self.width) -20 or self.rect.centerx <20 +(self.width):
            self.velx= -self.velx
            self.rect.centery +=50
            self.rect.x += self.velx

    def disparo(self,lista,vida):
        if isinstance (lista,list) and isinstance (vida,int):
            return self.disparo_aux(lista,vida,0,0)
        else: return "Error"

    def disparo_aux(self,lista,vida,resultado,indice):
        if indice == len(lista):
            return resultado
        elif isinstance(lista[indice],list):
            return self.disparo_aux(lista[indice],vida,0,0)+self.disparo_aux(lista,vida,resultado,indice+1)
        elif vida != 0:
            disparo_enemigo=(enemigo.rect.centerx,enemigo.rect.centery,2,10,"../imagenes/disparo_enemigo.jpg")
        #for enemigos in enemigo.list:
         #   if enemigos.health!=0:
          #      disparo_enemigo(enemy.rect.centerx,enemy.rect.centery,2,10,"../imagenes/disparo_enemigo.jpg")##cambiar direccion y nombre

    def revisar_vida(self,lista,vida):
        if isinstance (lista,list) and isinstance (vida,int):
            return self.revisar_vida_aux(lista,vida,0,0)
        else:
            return "Error"
                
    def revisar_vida_aux(self,lista,vida,resultado,indice):
        if indice==len(lista):
            return resultado
        elif isinstance(lista[indice], list):
            return (self.revisar_vida_aux(lista[indice],vida,0,0)+self.revisar_vida_aux(lista,vida,resultado,indice+1))
        elif vida==0:
            return False
        Naves.score+=5
        enemigo.image=pygame.image.load("../imagenes/explosiones.gif")
        enemigo.velx = 0
        enemigo.dead = True  #revisar aqui

    #@staticmethod
    #def revisar_vida():
     #   for enemigos in enemigo.lista:
      #      if enemigos.health==0:
       #         if enemu.dead==False:
        #            Naves.score+=5
         #           enemy.image=pygame.image.load("../imagenes/explosiones.gif")
          #          enemy.velx=0
           #         enemy.dead=True

##Clase disparo
class proyectil(pygame.sprite.Sprite):
    allproy= pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_string)
        self.rect=self.image.get_rect()
        self.height=height
        self.rect.x=x
        self.rect.y=y
        self.vely=-8
        proyectil.allproy.add(self)
        
class proyectil_jugador(proyectil):
    lista=pygame.sprite.Group()
    lista_normal=[]

    def __init__(self, x, y, width, height, image_string):
        proyectil.__init__(self, x, y, width, height, image_string)
        if len(proyectil_jugador.lista_normal)!=0:
            last_element = proyectil_jugador.lista_normal[-1]
            difference = abs(self.rect.y-last_element.rect.y)
            if difference <= self.height+50:
                proyectil.allproy.remove(self)
                proyectil_jugador.lista.add(self)

    
    def movimiento(height):
        for proyectil in proyectil_jugador.lista:
            proyectil.rect.y += proyectil.vely
            if proyectil.rect.y <10:
                proyectil.allproj.remove(proyectil)
                proyectil_enemigo.lista.remove(proyectil)
                del proyectil

class proyectil_enemigo(proyectil):
    lista=pygame.sprite.Group()
    lista_normal=[]
    def __init__(self,x,y,width,height,image_string):
        proyectil.__init__(self,x,y,width,height,image_string)
        self.vely=8
        if(len(proyectil_enemigo)!=0):
            last_element = proyectil_enemigo.lista_normal[-1]
            difference = abs(self.rect.y-last_element.rect.y)
            if difference <= self.height+10:
                proyectil.allproj.remove(self)
                return

            proyectil_enemigo.lista.add(self)
            proyectil_enemigo.lista_normal.append(self)

    @staticmethod
    def movement(height):
        for proyectil in proyectil_enemigo.lista:
            proyectil.rect.y += proyectil.vely
            if proyectil.rect.y <10:
                proyectil.allproj.remove(proyectil)
                proyectil_enemigo.lista.remove(proyectil)
                del proyectil

            elif proyectil.rect.y > height-10:
                proyectil.allproj.remove(proyectil)
                proyectil_jugador.lista.remove(proyectil)
                del proyectil
    
    
                  
                  
                                
                                
