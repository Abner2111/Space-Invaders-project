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

    def draw(self, surface): #"dibuja" a los objetos en pantalla
        surface.blit(slef.image, (self.rect.x-self.rect.width/2, self.rect.y-self.rect.height))
    def destroy(self, ClassName): #destruye sprite
        ClassName.List.remove(self)
        General.allsprites.remove(self)
        del self

    class Naves(General): #clase general de naves
        lista = pygame.sprite.Group
        score = 0

        def __init__(self,x ,y ,  ):


