##Clases
import pygame #####se llama las funciones de pygame 
##clase principal a usar
class General(pygame.sprite.Sprite):#Se crea una clase general para el manejo de los sprites(imagenes) que se van a usar para complementar el juego en su diseño.

    allsprites= pygame.sprite.Group()#funcion para los objetos de los juegos
    def __init__(self,x,y,width,height,image_string):# definicion de funcion para ubicacion,movimiento y aspecto de los objetos 
        pygame.sprite.Sprite.__init__(self)
        General.allsprites.add(self)
##definicion de los objetos y posiciones
        self.image= pygame.image.load(image_string)
        self.rect= self.image,get_rect()

        self.width=width
        self.height=height
        self.rect.centerx=x
        self.rect.centery=y
    def draw(self,surface):## funcion que se define para poner los objetos en movimiento y que puedan ser usados
        surface.blit(self.image,(self.rect.x-self.rect.width/2,self.rect.y-self.rect.height))

    def destroy(self,ClassName):### se define la funcion que destruira las naves
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
        self.health=150#vida de las naves
        self.velx=0# se establece la velocidad de las naves

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
        elif self.rect.centerx <20 +(self.width) and self.velx <0:#se establece ubicacion y velocidad del jugador
            self.velx=0## velocidad inicial
            self.rect.x += self.velx
    def revisar_vida(self,lista,vida):###funcion para revisar la vida
        if isinstance (lista,list) and isinstance (vida,int):# condicion de los valores que se usaran
            return self.revisar_vida_aux(lista,jugador.vida,0,0)# envia a la funcion a revisar la lista de indices
        else: return "Error"
                
    def revisar_vida_aux(self,lista,vida,resultado,indice):#se define la funcion para revisar la vida en una lista
        if indice==len(lista):# se establece la condicon de parada
            return resultado
        elif isinstance (lista[indice],list):
            return (self.revisar_vida_aux(lista[indice],vida,0,0)+self.revisar_vida_aux(lista,vida,resultado,indice+1))
        elif vida==0:# si la vida del jugador es 0, este vera la palabra "Game Over" sabiendo que perdio
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

class enemigo(Naves): #se define la clase del enemigo
    lista=pygame.sprite.Group()# se define el tipo de esta clase
    def __init__(self,x,y,width,height,image_string):# se define la posicion 
        Naves.__init__(self,x,y,height,image_string)
        enemigo.lista.add(self)
        self.dead=False
        self.velx=3#se establece la velocidad
        self.daño_recibido=50#se establecel daño que puede recibir

    def movimiento(self,SCREENWIDTH):# se define la posicion de los enemigos en la pantalla y los movimientos que podra realizar
        if self.rect.centerx > SCREENWIDTH - (self.width) -20 or self.rect.centerx <20 +(self.width):# es establece la ubicacion en la pantalla
            self.velx= -self.velx# se define la velocidad de las naves
            self.rect.centery +=50# se define la posicion que estaran
            self.rect.x += self.velx

    def disparo(self,lista,vida):# se define la vida del enemigo
        if isinstance (lista,list) and isinstance (vida,int):
            return self.disparo_aux(lista,vida,0,0)# se devuelve a revisar la vida del enemigo
        else: return "Error"

    def disparo_aux(self,lista,vida,resultado,indice):#se define la funcion axuliar para revisar los indices, sobre el daño y lso disparos
        if indice==len(lista):
            return resultado
        elif isinstance (lista[indice],list):
            return self.disparo_aux(lista[indice],vida,0,0)+self.disparo_aux(lista,vida,resultado,indice+1)
        elif vida !=0:
            disparo_enemigo(enemigo.rect.centerx,enemigo.rect.centery,2,10,"../imagenes/disparo_enemigo.jpg") # se define la imagen que tendra los disparos
        #for enemigos in enemigo.list:
         #   if enemigos.health!=0:
          #      disparo_enemigo(enemy.rect.centerx,enemy.rect.centery,2,10,"../imagenes/disparo_enemigo.jpg")##cambiar direccion y nombre

    def revisar_vida(self,lista,vida):# se define una funcion para revisar la vida
        if isinstance (lista,list) and isinstance (vida,int):
            return self.revisar_vida_aux(lista,vida,0,0)# se repite los pasos similares a los anteriores
        else: return "Error"
                
    def revisar_vida_aux(self,lista,vida,resultado,indice):
        if indice==len(lista):
            return resultado
        elif isinstance (lista[indice],list):
            return (self.revisar_vida_aux(lista[indice],vida,0,0)+self.revisar_vida_aux(lista,vida,resultado,indice+1))
        elif vida==0:# si la vida del enemigo es 0 se le da al jugador los puntos
            return False
        Naves.score+=5
        enemigo.image=pygame.image.load("../imagenes/explosiones.gif") #se define la imagen que se vera al destruir un enemigo
        enemy.velx=0
        enemy.dead=True #se establece que el cuando el enemigo esta muerto es verdadero

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
class proyectil(pygame.sprite.Sprite):# se establece la clase de los proyectiles y sus caracteristicas, acciones que tiene, velocidad, posicion que tendran estos
    allproy= pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_string)# se establece que los disparos tendran imagenes
        self.rect=self.image.get_rect()
        self.height=height
        self.rect.x=x
        self.rect.y=y
        self.vely=-8
        proyectil.allproj.add(self)
        
class proyectil_jugador(proyectil):# se define la clase del proyectil del jugador
    lista=pygame.sprite.Group()
    lista_normal=[]
    def __init__(self,x,y,width,height,image_string):# se establecen de las caracterisiticas del proyectil del jugador
        proyectil__init__(self,x,y,width,height,image_string)
        if (len(proyectil_jugador.lista_normal)!=0):
            last_element=proyectil_jugador.normal_list[-1]
            difference= abs(self.rect.y-last_element.rect.y)
            if difference <= self.height+50:
                proyectil.allproj.remove(self)
                return proyectil_jugador.lista.add(self)

    
    def movimiento(self, height): # se define la funcion del movimiento del jugador
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
    def movimiento(height):
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
    
    
                  
                  
                                
                                
