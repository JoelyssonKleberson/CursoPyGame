import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 700
altura = 500
x = largura/2
y = altura/2

x_azul = randint(40, 680)
y_azul = randint(50, 480)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f"Pontos: {pontos}"
    texto_pontos = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
#Clicando:

        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         x = x - 20
        #     if event.key == K_d:
        #         x = x + 20
        #     if event.key == K_w:
        #         y = y - 20
        #     if event.key == K_s:
        #         y = y + 20
#Segurando:

    if pygame.key.get_pressed()[K_a]:
        x = x - 20    
    if pygame.key.get_pressed()[K_d]:
        x = x + 20    
    if pygame.key.get_pressed()[K_w]:
        y = y - 20    
    if pygame.key.get_pressed()[K_s]:
        y = y + 20    
    
    retangulo_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    retangulo_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))

    if retangulo_vermelho.colliderect(retangulo_azul):
        x_azul = randint(40, 680)
        y_azul = randint(50, 480)
        pontos += 1
    
    tela.blit(texto_pontos, (450, 50))
    
    pygame.display.update()
