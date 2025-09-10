import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(1)

musica_de_fundo = pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(-1)

som_colissao = pygame.mixer.Sound('som.wav')
som_colissao.set_volume(1)

largura = 700
altura = 500

x_cobra = int(largura/2)
y_cobra = int(altura/2)

velocidade_cobra = 10
x_controle = velocidade_cobra
y_controle = 0

x_maca = randint(40, 680)
y_maca = randint(50, 480)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()


lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumentar_tamanho_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu

    pontos = 0
    comprimento_inicial = 5

    x_cobra = int(largura/2)
    y_cobra = int(altura/2) 
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 680)
    y_maca = randint(50, 480)
    morreu = False

while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f"Pontos: {pontos}"
    texto_pontos = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade_cobra:
                    pass
                else:
                    x_controle = -velocidade_cobra
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade_cobra:
                    pass
                else:
                    x_controle = velocidade_cobra
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade_cobra:
                    pass
                else:
                    y_controle = -velocidade_cobra
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade_cobra:
                    pass
                else:
                    y_controle = velocidade_cobra
                    x_controle = 0

    x_cobra += x_controle
    y_cobra += y_controle
    
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 680)
        y_maca = randint(50, 480)
        pontos += 1
        som_colissao.play()
        comprimento_inicial += 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte_morte = pygame.font.SysFont('arial', 20, True, True)
        mensagem_morte = "Game Over! Pressione a Tecla \'R\' para Tentar Novamente!"
        texto_morte = fonte_morte.render(mensagem_morte, True, (0,0,0))
        retangulo_texto = texto_morte.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            retangulo_texto.center = (largura//2, altura//2)
            tela.blit(texto_morte, retangulo_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumentar_tamanho_cobra(lista_cobra)

    tela.blit(texto_pontos, (450, 50))
    
    pygame.display.update()
