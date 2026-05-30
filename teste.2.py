from operator import truediv

import pygame
from pygame.locals import *
from sys import exit
from random import randint, choice
pygame.init()
pygame.mixer.music.set_volume(0.25)
musica_de_fundo = pygame.mixer.music.load("Pumpupthemind - Coffee Cup.mp3")
pygame.mixer.music.play(-1)
#musica_de_fundo.set_volume(0.5)
ponto_musica = pygame.mixer.Sound("smw_1-up.wav")
ponto_musica.set_volume(0.75)
larg = 980
alti = 820
y_cobra = alti / 2 - 50 / 2 # Y = altura
x_cobra= larg / 2 - 50 / 2 # X = largura
pontos = 0
fonte = pygame.font.SysFont("Arial", 40, True, True)
x_apple = randint(40, larg-40)
y_apple = randint(40, alti-40)
velocidade = 10
x_controle = -velocidade
y_controle = 0
lista_parabens =['Isso Aí!', 'Parabéns!', 'COLISÃO!', ';)']
parabens = ''
pygame.display.set_caption("Pygame")
tela = pygame.display.set_mode((larg, alti))
pygame.display.set_caption('Teste')
relogio = pygame.time.Clock()
def aumenta_corpo(lista_corpo):
    for corpo in lista_corpo:
        pygame.draw.rect(tela, (0, 255, 0), (corpo[0], corpo[1], 50, 50))
def reiniciar_jogo():
    global pontos, corpo_inicial, y_cobra, x_cobra, lista_corpo, lista_cabeca, x_apple, y_apple, morte
    pontos = 0
    corpo_inicial = 2.5
    y_cobra = alti / 2 - 50 / 2  # Y = altura
    x_cobra = larg / 2 - 50 / 2  # X = largura
    lista_corpo = []
    lista_cabeca = []
    x_apple = randint(40, 600)
    y_apple = randint(40, 440)
    morte = False
lista_corpo = []
corpo_inicial = 2.5
while True:
    tela.fill((255,255,255))
    relogio.tick(60)
    msg = f"Pontos: {pontos}"
    para = f"{parabens}"
    txt_formatado = fonte.render(msg, True, (0,0,0))
    txt_parabens = fonte.render(para, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if x_controle > 0:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if x_controle < 0:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if y_controle > 0:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if y_controle < 0:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
    x_cobra = x_controle + x_cobra
    y_cobra = y_controle + y_cobra
    cobra = pygame.draw.rect(tela, (0, 255, 0),(x_cobra, y_cobra, 50,50))
    apple = pygame.draw.rect(tela, (255, 0, 255), (x_apple, y_apple, 40, 40))
    if cobra.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(40, 440)
        tempo_ultimo_spawn = pygame.time.get_ticks()
        #print("COLIDIU!!!") or  print("ISSO Aí!!!")
        pontos += 1
        ponto_musica.play()
        ult = parabens
        parabens = choice(lista_parabens)
        while parabens == ult:
            parabens = choice(lista_parabens)
        corpo_inicial = corpo_inicial + 2.5
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_corpo.append(lista_cabeca)
    if lista_corpo.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont("Arial", 20, True, True)
        mesg_final = f'Game Over! Pressione R para continuar!'
        txt_final = fonte2.render(mesg_final, True, (0, 0, 0))
        ret_txt = txt_final.get_rect()
        ret_txt.center = (larg // 2, alti // 2)
        morte = True
        while (morte):
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reiniciar_jogo()
            tela.blit(txt_final, ret_txt)
            pygame.display.update()
    if x_cobra > larg:
        x_cobra = 0
    if y_cobra > larg:
        y_cobra = 0
    if x_cobra < 0:
        x_cobra = larg
    if y_cobra < 0:
        y_cobra = larg
    aumenta_corpo(lista_corpo)
    if len (lista_corpo) > (corpo_inicial):
        del lista_corpo[0]
    tela.blit(txt_formatado, (larg-255, 40))
    tela.blit(txt_parabens, (larg-255, 90))
    pygame.display.update()