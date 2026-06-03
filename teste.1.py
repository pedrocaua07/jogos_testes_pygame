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
larg = 640
alti = 480
y = 0 # Y = altura
x = larg/2 - 50/2 # X = largura
pontos = 0
fonte = pygame.font.SysFont("Arial", 40, True, True)
x_azul = randint(40, 600)
y_azul = randint(40, 440)
# --- NOVO: Variável para controlar o tempo do Spawn ---
tempo_ultimo_spawn = pygame.time.get_ticks()
tempo_espera = 1500  # Tempo em milissegundos (2000 ms = 2 segundos)
lista_parabens =['Boa Manu!!', 'Parabéns!', 'COLISÃO!', ';)']
parabens = ''
pygame.display.set_caption("Pygame")
tela = pygame.display.set_mode((larg, alti))
pygame.display.set_caption('Teste')
relogio = pygame.time.Clock()
while True:
    tela.fill((0,0,0))
    relogio.tick(60)
    msg = f"Pontos: {pontos}"
    para = f"{parabens}"
    txt_formatado = fonte.render(msg, True, (255,255,255))
    txt_parabens = fonte.render(para, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x += -20
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x += 20
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                y += -20
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                y += 20
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        x -= 10
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        x += 10
    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        y -= 10
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        y += 10
        # --- NOVO: Limitador para o jogador não sair da tela ---
    if x < 0:
        x = 0
    if x > larg - 50:  # 50 é a largura do quadrado vermelho
        x = larg - 50
    if y < 0:
        y = 0
    if y > alti - 50:  # 50 é a altura do quadrado vermelho
        y = alti - 50
        # --- NOVO: Lógica do Cronômetro para mudar o azul de lugar ---
    tempo_atual = pygame.time.get_ticks()
        # Se a diferença do tempo atual para o último spawn for maior que 2 segundos:
    if tempo_atual - tempo_ultimo_spawn > tempo_espera:
        x_azul = randint(40, 600)
        y_azul = randint(40, 440)
        tempo_ultimo_spawn = tempo_atual  # Reinicia o cronômetro
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0),(x, y, 50,50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 40))
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(40, 440)
        tempo_ultimo_spawn = pygame.time.get_ticks()
        #print("COLIDIU!!!") or  print("ISSO Aí!!!")
        pontos += 1
        ponto_musica.play()
        ult = parabens
        parabens = choice(lista_parabens)
        while parabens == ult:
            parabens = choice(lista_parabens)
    tela.blit(txt_formatado, (425, 40))
    tela.blit(txt_parabens, (425, 90))
    pygame.display.update()