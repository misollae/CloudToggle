from reversi_motor_48584 import reversi_jogada_possivel
from random import random
from random import choice

def jogada_agente(jogo):
    escolhas = []
    for il in range(8): # O agente vai correr todas as linhas
        for ic in range(8): # E todas as colunas
            # Vai verificar se a jogada nessa posição é válida
            if reversi_jogada_possivel(jogo, il + 1, ic + 1) == True:
            # Se for, vai juntar a linha e a coluna a uma lista 
                jogavel = (il + 1, ic + 1)
                escolhas.append(jogavel)
    # Por fim, vai escolher uma dessas posições à sorte
    jogada = choice(escolhas)
    return jogada
