import pygame
from pygame.locals import *
from sys import exit 

pygame.init()

largura = 640
altura = 480

cor_preto = (0,0,0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

class Gato(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('cat_sprites/sprite_0.png'))
        self.sprites.append(pygame.image.load('cat_sprites/sprite_1.png'))
        self.sprites.append(pygame.image.load('cat_sprites/sprite_2.png'))
        self.sprites.append(pygame.image.load('cat_sprites/sprite_3.png'))
        self.sprites.append(pygame.image.load('cat_sprites/sprite_4.png'))
        self.sprites.append(pygame.image.load('cat_sprites/sprite_5.png'))
        self.sprites.append(pygame.image.load('cat_sprites/sprite_6.png'))
        self.sprites.append(pygame.image.load('cat_sprites/sprite_7.png'))
        self.sprites.append(pygame.image.load('cat_sprites/sprite_8.png'))
        self.sprite_atual = 0
        self.image = self.sprites[self.sprite_atual]
        self.image = pygame.transform.scale(self.image, (32*4, 32*4))

        self.rect = self.image.get_rect()
        self.rect.topleft = 50, 250

    def update(self):
        self.sprite_atual += 0.5
        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0
        self.image = self.sprites[int(self.sprite_atual)]
        self.image = pygame.transform.scale(self.image, (32*4, 32*4))

todas_as_sprites = pygame.sprite.Group()
gato = Gato()
todas_as_sprites.add(gato)

imagem_fundo = pygame.image.load('cat_sprites/city_background.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(15)
    tela.fill(cor_preto)
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
    tela.blit(imagem_fundo, (0,0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
