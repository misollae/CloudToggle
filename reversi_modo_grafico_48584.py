#            ISEL
#   Reversi - Modo Gráfico
#   Letícia Lucas - A48584

import pygame

# funções do interface com o motor
from reversi_motor_48584 import reversi_novo_jogo
from reversi_motor_48584 import reversi_valor
from reversi_motor_48584 import reversi_jogada_possivel
from reversi_motor_48584 import reversi_fim_jogo
from reversi_motor_48584 import reversi_proximo_a_jogar
from reversi_motor_48584 import reversi_pontuacao
from reversi_motor_48584 import reversi_jogar

# função do interface com o agente
from reversi_agente_48584 import jogada_agente


pygame.mixer.init()
pygame.mixer.pre_init(44100,16,2,4096) # Iniciação do mixer (frequencia, bits, saidas, buffer)
pygame.init()
placing = pygame.mixer.Sound('place.wav') # Efeitos sonoros

# Criar uma janela gráfica:

largura = 1170
altura  = 732
size    = [largura,altura]               
screen  = pygame.display.set_mode(size)  
pygame.display.set_caption("Cloud Toggle - Letícia Lucas") 
clock = pygame.time.Clock()


                                # Livraria de Imagens Usadas #
# Grelha, contruida com várias peças disponiveis online -------------------------------
background      = pygame.image.load("grelhanuvens3.png") 
background      = pygame.transform.scale(background, (1170, 732)) # Escalamento da imagem

# Sprites jogáveis, escolhidas de listas disponibilizadas, e posteriormente editadas --
sprite1         = pygame.image.load("sprite1.png")
winner1         = pygame.image.load("winnerraccoon.png")
sprite2         = pygame.image.load("sprite2.png")
winner2         = pygame.image.load("winneryellow.png")
draw            = pygame.image.load("draw.png")
points          = pygame.image.load("points.png")
clouds          = pygame.image.load("winnerclouds.png")
keys            = pygame.image.load("keys.png")


# Fundo de nuvems, editado ------------------------------------------------------------
bg              = pygame.image.load("bg.jpg")

# Setas de posição, editadas ----------------------------------------------------------
arrow1          = pygame.image.load("arrow1.png")

# Sprite de personagem de um antigo jogo, com material agora público ------------------
notary          = pygame.image.load("notary.png")
notary          = pygame.transform.scale(notary, (121, 143))

background.set_colorkey((0, 0, 0))
clouds.set_colorkey((0, 0, 0))
sprite1.set_colorkey((0, 0, 0))
winner1.set_colorkey((0, 0, 0))
keys.set_colorkey((0, 0, 0))
notary.set_colorkey((0, 0, 0))  # Estas linhas permitem eliminar o fundo preto (RGB 0,0,0) das imagens
sprite2.set_colorkey((0, 0, 0)) # Ignorando totalmente essa cor
winner2.set_colorkey((0, 0, 0))
draw.set_colorkey((0, 0, 0))
points.set_colorkey((0, 0, 0))
arrow1.set_colorkey((0, 0, 0))


                                  # Definição de Funções do Jogo #
                                  
# 1. Função que transforma o click do jogador uma jogada ------------------

def get_click(pos):
    x = pos[0] # x vai ser o primeiro elemento das coordenadas lidas
    y = pos[1] # e y será o segundo
    
    # Inicia-se uma variável, começando em 0 até 7, 8 valores, um para cada linha
    for aumento in range(8):
        desvio = aumento * 27
        # o desvio entre linhas e colunas é de cerca de 27 pixeis, daí a múltiplicação pelo indice
        if 460 + desvio <= x <= 487 + desvio:
        # x=460 e x=487 são as fronteiras da primeira coluna, as coordenadas aumentam de 27 em 27
            coluna = 1 + aumento
        if 293 + desvio <= y <= 320 + desvio:
        # y=293 e y=320 são as fronteiras da primeira coluna, as coordenadas aumentam de 27 em 27
            linha = 1 + aumento
            
    return (linha, coluna) # Devolve a coluna em que se fez o click!


# 2. Colocação dos Pontos --------------------------------------------------

def notario_pontos (pontos):
    font           = pygame.font.SysFont("Comic Sans MS", 21)        # Fonte e tamanho
    pontos_jogador = font.render(str(pontos[0]), 1, (196, 167, 151)) # texto e cor RGB
    pontos_agente  = font.render(str(pontos[1]), 1, (252, 220, 124))
    screen.blit(pontos_jogador, (846, 308))                          # Coordenadas
    screen.blit(pontos_agente,  (846, 283))



# 3. Print da Grelha -------------------------------------------------------
  
def grelha(jogo):
    screen.blit(notary, (780, 135)) # Colocação de alguns sprites
    screen.blit(points, (800, 280))
    screen.blit(keys, (10, 10))

    y=293 
    for linha in [1,2,3,4,5,6,7,8]:
        x=460                            # contagem das colunas recomeça sempre que muda de linha
        for coluna in [1,2,3,4,5,6,7,8]: 
            if reversi_jogada_possivel(jogo, linha, coluna): # Se o jogador puder jogar nesta posição
                if jogo[1] == 1:                             # só na vez do jogador
                    screen.blit(arrow1, [x,y])               # aparece uma seta.
            if reversi_valor(jogo, linha, coluna) == 1:      # Se a posição estiver ocupada
                screen.blit(sprite1, [x,y])                  # Mostrará um dos monstros
            if reversi_valor(jogo, linha, coluna) == 2: 
                screen.blit(sprite2, [x,y])
            x=x+27  # Diferença de  cerca de 27 pixeis entre linhas e colunas
        y=y+27


# Inicialização de um novo jogo
jogo = reversi_novo_jogo()
pygame.mixer.music.load("librarians.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
screen.blit(bg, (0, 0))


# gestao do jogo:
cloud_toggle = True # Esta variável será True enquanto o jogador continuar a jogar, ou seja, durante a vida do programa é sempre verdadeira!

while cloud_toggle:
    for event in pygame.event.get():    

        grelha(jogo)
       
        (proximo_a_jogar, jogador_que_passou) = reversi_proximo_a_jogar(jogo)
    
        if proximo_a_jogar == 1: # Se o jogador carregar na grelha na sua vez de jogar,
                                 # é lida e validada a sua posição, passando então à jogada
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if 460 <= x <= 676 and 293 <= y <= 509: # se o clique for na grelha
                    (linha, coluna) = get_click(pos)
                    jogo = reversi_jogar(jogo, linha, coluna)
                    placing.play()
                
                
        else: # Jogada do agente!
            pygame.time.wait(700)
            reversi_jogar(jogo, linha, coluna)
            (linha, coluna) = jogada_agente(jogo)
            placing.play()
            jogo = reversi_jogar(jogo, linha, coluna)

        screen.blit(background, [0,0]) 
        grelha(jogo)
        pontos         = reversi_pontuacao(jogo)
        notario_pontos(pontos)

        if reversi_fim_jogo(jogo): # Prints dos vencedores
            screen.blit(clouds, [380,320])
            if pontos[0] > pontos[1]:
                screen.blit(winner1, [590,350])
            elif pontos[0] < pontos[1]:
                screen.blit(winner2, [590,350])
            elif pontos[0] == pontos[1]:
                screen.blit(draw, [465,370])
                
        if event.type == pygame.KEYDOWN: # Quando se prime..
            if event.key == pygame.K_n:     # tecla n - novo jogo
                jogo = reversi_novo_jogo()
            if event.key == pygame.K_q:     # tecla q - sair do jogo
                pygame.quit()
                
    pygame.display.flip()                   # limpar o estado da janela
    clock.tick(10)                          # 10 frames por segundo

