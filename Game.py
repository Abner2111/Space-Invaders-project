import Clases
from Clases import *
import cvs_json
import random
pygame.init ()

run = True
game = False

screen_size = [1280, 720] #tamano de la pantalla
win = pygame.display.set_mode ((screen_size[0], screen_size[1])) #superficie principal

fuente1 = pygame.font.Font('fonts/space_invaders.ttf', 48) #fuente a usar tamano 48
fuente2 = pygame.font.Font('fonts/space_invaders.ttf', 28) #fuente a usar tamano 48
pygame.display.set_caption("Space Invaders")


background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (1280, 720))
back_rect = background.get_rect()


def rand_screen(): #decide aleatoriamente un banner y colores de botones
    opciones = [['images/banner 2.png', (54, 86, 101), (52, 28, 121), (254, 254, 15)],
                ['images/banner.png', (84, 0, 10), (166, 0, 19), (255, 226, 23)]]
    return random.choice(opciones)

menu_format = rand_screen()

banner = pygame.image.load(menu_format[0])
banner = pygame.transform.scale(banner, (1280, 330))
texto_jugar = fuente1.render('JUGAR', True, menu_format[3]) #fuente del boton de jugar
texto_top = fuente2.render('5 MEJORES', True, menu_format[3]) #fuente del top

win.blit(background, (0, 0))
win.blit(banner, (0, 0))
bac_boton = pygame.draw.rect(win, menu_format[1], (490, 400, 300, 100))
front_boton = pygame.draw.rect(win, menu_format[2], (500, 410, 280, 100))
win.blit(texto_top, (560, 535))
win.blit(texto_jugar, (550, 435))



matriz_enemigos = []


def menu ():
    pass


while run:
    pygame.time.delay (10)
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:  # evento presionar equis
            run = False  # cierra el ciclo pincipal
    if game:
        pass

    pygame.time.delay (10)
    pygame.display.update ()

pygame.quit ()
