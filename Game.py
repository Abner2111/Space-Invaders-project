from Clases import *
import csv_json
import random

pygame.init()
run = True
game = False
game_running = False
file_manager = CSV()

white = (255, 255, 255)

#VARIABLES DE PANTALLA
screen_size = [1280, 720] #tamano de la pantalla
win = pygame.display.set_mode ((screen_size[0], screen_size[1])) #superficie principal
pygame.display.set_caption("Space Invaders")

#FUENTES
fuente1 = pygame.font.Font('fonts/space_invaders.ttf', 48) #fuente a usar tamano 48
fuente2 = pygame.font.Font('fonts/space_invaders.ttf', 28) #fuente a usar tamano 48

#FONDO DEL JUEGO
background = pygame.image.load('images/background.png')
background = pygame.transform.scale(background, (1280, 720))
back_rect = background.get_rect()

#MUSICA DE FONDO MENU
pygame.mixer.music.load('sounds\menu_music.mp3')

pygame.mixer.music.play(-1)



#nave jugador
jugador = Jugador(640, 720, 60, 60, 'images/jugador.png')



def rand_screen(): #decide aleatoriamente un banner y colores de botones
    opciones = [['images/banner 2.png', (54, 86, 101), (52, 28, 121), (254, 254, 15)],
                ['images/banner.png', (84, 0, 10), (166, 0, 19), (255, 226, 23)]]
    return random.choice(opciones)

menu_format = rand_screen()


texto_jugar = fuente1.render('JUGAR', True, menu_format[3]) #fuente del boton de jugar
texto_top = fuente2.render('5 MEJORES', True, menu_format[3]) #fuente del top


def game_screen():
    jugador.draw(win)

def main_menu(): #
    global texto_jugar, texto_top, game
    banner = pygame.image.load(menu_format[0])
    banner = pygame.transform.scale(banner, (1280, 330))
    win.blit(background, (0, 0))
    win.blit(banner, (0, 0))
    bac_boton = pygame.draw.rect(win, menu_format[1], (490, 400, 300, 100))
    front_boton = pygame.draw.rect(win, menu_format[2], (500, 410, 280, 100))
    win.blit(texto_top, (560, 535))
    win.blit(texto_jugar, (550, 435))



    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 500 < mouse[0] < 780 and 410 < mouse[1] < 510:
        if click[0]:
            texto_jugar = fuente1.render('JUGAR', True, menu_format[3])
            pygame.time.delay(50)
            game = True
            win.blit (background, (0, 0))
            game_screen()
        else:
            texto_jugar = fuente1.render('JUGAR', True, white)
    else:
        texto_jugar = fuente1.render('JUGAR', True, menu_format[3])

    if 560 < mouse[0] < 740 and 535 < mouse[1] < 585:
        if click[0]:
            texto_top = fuente2.render('5 MEJORES', True, menu_format[3])
            pygame.time.delay(50)
            print("top")
        texto_top = texto_top = fuente2.render('5 MEJORES', True, white)
    else:
        texto_top = fuente2.render('5 MEJORES', True, menu_format[3])


matriz_enemigos = []


while run:

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # evento presionar equis
            run = False  # cierra el ciclo pincipal
    if game:
        if game_running:
            if keys[pygame.K_a]:
                jugador.cambia_vel([-5, 0])
                jugador.move()
                win.blit(background, (0, 0))
                jugador.draw(win)
            if keys[pygame.K_d]:
                jugador.cambia_vel([5, 0])
                jugador.move()
                win.blit(background, (0, 0))
                jugador.draw(win)
            if keys[pygame.K_w]:
                jugador.cambia_vel([0, -5])
                jugador.move()
                win.blit(background, (0, 0))
                jugador.draw(win)
            if keys[pygame.K_s]:
                jugador.cambia_vel([0, 5])
                jugador.move()
                win.blit(background, (0, 0))
                jugador.draw(win)

        else:
            game_screen()
            game_running = True
    else:
        main_menu()

    pygame.display.update()

pygame.quit()
