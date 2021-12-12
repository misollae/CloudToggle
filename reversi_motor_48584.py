        # ISEL
# Motor do jogo  Reversi
# Letícia Lucas 48584

# funções:
def get_posicoes_vazias(grelha):
# Esta função vai procurar as posições vazias da grelha
    posicoes_vazias = []
    for il in range(len(grelha)):
        for ic in range (len(grelha[il])):
            if grelha[il][ic] == 0: # Está vazia se o elemento da lista for 0
                vazio = (il, ic)
                posicoes_vazias.append(vazio)
    return posicoes_vazias

def get_outro_jogador(jogador): # Dado um jogador, retorna o outro
    if jogador == 1:
        return 2
    if jogador == 2:
        return 1

def fora_tabuleiro(linha, coluna): # Verifica se a peça está no tabuleiro
    if 1 <= linha <= 8 and 1 <= coluna <= 8:
        return False
    else:
        return True

def mudar_peca(jogo, linha, coluna):
# Esta função muda uma posição na grelha para uma peça do jogador
    grelha  = jogo[0]
    jogador = jogo[1]
    grelha[linha - 1][coluna - 1] == jogador
    return grelha

def get_peca(grelha, linha, coluna):
# Esta função retorna a peça na posição indicada
    if fora_tabuleiro(linha, coluna) == False:
        return grelha[linha - 1][coluna - 1]

def get_pecas_a_virar(grelha, jogador, linha, coluna):
    pecas_a_virar = []
    opositor   = get_outro_jogador(jogador)
    
    # A viragem acontece num sentido positivo e num sentido negativo:
    for desvio in [-1, 1]:
        col_incrementada = coluna + desvio # Vamos  sempre começar por olhar para as peças que se 
        lin_incrementada =  linha + desvio # Encontram adjacentes à jogada estudada

        # Começamos por virar nas linhas:
        if get_peca(grelha, linha, col_incrementada) == opositor: # Se a peça adjecente for do opositor...
            # Enquanto estiver na grelha                e ainda for do opositor...
            while 1 <= col_incrementada <= 8 and get_peca(grelha, linha, col_incrementada) == opositor:
                # Continua-se o caminho na direção...
                col_incrementada = col_incrementada + desvio
                # Se antes de se chegar ao fim se encontrar uma peça do jogador, a jogada é válida
                if get_peca(grelha, linha, col_incrementada) == jogador:
                    # E inicia-se o movimento de "volta" para guardar todas as peças confirmadas como do opositor
                    col_incrementada = col_incrementada - desvio
                    while col_incrementada != coluna: # Só se para ao voltar à posição inicial
                        pecas_a_virar.append([linha, col_incrementada]) # Até lá, guardam-se as posições numa lista
                        col_incrementada = col_incrementada - desvio

        col_incrementada = coluna + desvio # Reinicialização
        lin_incrementada =  linha + desvio

        # E a mesma ideia para as colunas...
        if get_peca(grelha, lin_incrementada, coluna) == opositor:
            while 1 <= lin_incrementada <= 8 and get_peca(grelha, lin_incrementada, coluna) == opositor:
                lin_incrementada = lin_incrementada + desvio
                if get_peca(grelha, lin_incrementada, coluna) == jogador:
                    lin_incrementada = lin_incrementada - desvio
                    while lin_incrementada != linha:
                        pecas_a_virar.append([lin_incrementada, coluna])
                        lin_incrementada = lin_incrementada - desvio

        col_incrementada = coluna + desvio
        lin_incrementada =  linha + desvio

        # E diagonais!
        if get_peca(grelha, lin_incrementada, col_incrementada) == opositor:
            while 1 <= lin_incrementada <= 8 and 1 <= col_incrementada <= 8 and get_peca(grelha, lin_incrementada, col_incrementada) == opositor:
                lin_incrementada = lin_incrementada + desvio
                col_incrementada = col_incrementada + desvio
                if get_peca(grelha, lin_incrementada, col_incrementada) == jogador:
                    lin_incrementada = lin_incrementada - desvio
                    col_incrementada = col_incrementada - desvio
                    while lin_incrementada != linha:
                        pecas_a_virar.append([lin_incrementada, col_incrementada])
                        lin_incrementada = lin_incrementada - desvio
                        col_incrementada = col_incrementada - desvio

        col_incrementada = coluna - desvio
        lin_incrementada =  linha + desvio
        if get_peca(grelha, lin_incrementada, col_incrementada) == opositor:
            while 1 <= lin_incrementada <= 8 and 1 <= col_incrementada <= 8 and get_peca(grelha, lin_incrementada, col_incrementada) == opositor:
                lin_incrementada = lin_incrementada + desvio
                col_incrementada = col_incrementada - desvio
                if get_peca(grelha, lin_incrementada, col_incrementada) == jogador:
                    lin_incrementada = lin_incrementada - desvio
                    col_incrementada = col_incrementada + desvio
                    while lin_incrementada != linha:
                        pecas_a_virar.append([lin_incrementada, col_incrementada])
                        lin_incrementada = lin_incrementada - desvio
                        col_incrementada = col_incrementada + desvio
                    
    return pecas_a_virar


def is_valida(grelha, jogador): # Vai retornar um tuplo das posições jogáveis e peças a virar, cada um uma lista onde o mesmo
                                # indice em cada uma correspondem respetivamente à posição e às peças viraveis nessa mesma posição
    validas = []
    virar   = []
    for il in range(8):
        for ic in range(8): 
            if grelha[il][ic] == 0 and fora_tabuleiro(il + 1, ic + 1) == False: # Se estiver vazia e dentro do tabuleiro
                pecas_a_virar = get_pecas_a_virar(grelha, jogador, il + 1, ic + 1)                
                if len(pecas_a_virar) > 0:
                    validas.append([il + 1, ic + 1])
                    virar.append(pecas_a_virar)

    return validas, virar

def reversi_novo_jogo():
    # Esta função vai iniciar um novo jogo, isto é, obtém um tabuleiro novo:
    grelha  = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], # Legenda:
            [0, 0, 0, 1, 2, 0, 0, 0], ## 0 -> posições vazias
            [0, 0, 0, 2, 1, 0, 0, 0], ## 1 -> peças do jogador um, primeiro a jogar
            [0, 0, 0, 0, 0, 0, 0, 0], ## 2 -> peças do jogador dois, segundo a jogar
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]

    # O inicio do jogo é sempre igual:
    proximo_a_jogar     = 1 # primeiro jogador
    jogadas_possiveis   = [[3, 5], [4, 6], [5, 3], [6, 4]] # jogadas iniciais
    # pecas_a_conquistar é uma lista onde cada lista corresponde à posicão das
    # peças que podem ser conquistadas ao jogar na posição de jogadas_possiveis
    # com o mesmo indice
    pecas_a_conquistar  = [[[4, 5]], [[4, 5]], [[5, 4]], [[5, 4]]]
    # inicializa com nenhuma passagem
    jogador_que_passou  = None
    # armazenamento do jogo:
    jogo = [grelha, proximo_a_jogar, jogadas_possiveis,
            pecas_a_conquistar, jogador_que_passou]

    
    return jogo



def reversi_valor (jogo, linha, coluna):
# Esta função vai devolver o valor numa determinada posição do tabuleiro/grelha,
    grelha = jogo[0] # que se encontra armazenado no primeiro elemento da lista jogo
    valor = grelha[linha - 1][coluna - 1] #   primeira linha -> indice 0, daí o -1
    return valor



def reversi_jogada_possivel(jogo, linha, coluna):
    jogadas_possiveis = jogo[2]    
    for num in range(len(jogadas_possiveis)):  # vai ver a lista de todas as jogadas válidas...
        if [linha, coluna] == jogadas_possiveis[num]: # se a jogada introduzida estiver na lista
            return True # retorna True
    return False


    
def reversi_fim_jogo(jogo):
# Vai verificar se há casas "jogáveis"
  if len(jogo[2]) == 0: # Se não houver, o jogo acabou
    return True
  else:
    return False



    
def reversi_proximo_a_jogar(jogo): # Esta função vai retornar o jogador seguinte, verificando se algum teve que passar
    jogador = jogo[1] # suposto próximo
    procura = is_valida(jogo[0], jogador)
    jogadas = procura[0]
    
    if len(jogadas) != 0: # Se o jogador que supostamente jogaria asseguir tiver jogadas possiveis..
        proximo_a_jogar    = jogador     # é ele a jogar
        jogador_que_passou = None        # e ninguém passa

    else:
        proximo_a_jogar    = get_outro_jogador(jogador)  # se não, será o outro jogador a jogar
        jogador_que_passou = jogador                     # e houve uma passagem

    return (proximo_a_jogar, jogador_que_passou)




def reversi_pontuacao(jogo):
# Esta função vai contar o número de peças de cada jogador, cada peça equivale a 1 ponto, retornando um tuplo com a
# pontuação dos 2 jogadores
    grelha = jogo[0]
    pontos_jogador_1 = 0
    pontos_jogador_2 = 0
    for l in range(len(grelha)): # Correr linhas
        for c in range(len(grelha[l])): # Correr colunas
            if grelha[l][c] == 1: # se for um 1
                pontos_jogador_1 = pontos_jogador_1 + 1 # aumenta a pontuaçao do jogador por 1 valor
            elif grelha[l][c] == 2: # mesmo para o jogador 2!
                pontos_jogador_2 = pontos_jogador_2 + 1
    return (pontos_jogador_1, pontos_jogador_2)



def reversi_jogar(jogo, linha, coluna):
    grelha             = jogo[0]   # nomeação das variáveis armazenadas para facilitar leitura do código
    jogador            = jogo[1]
    jogadas_possiveis  = jogo[2]
    pecas_a_conquistar = jogo[3]
    
    for num in range(len(jogadas_possiveis)):       # Vai procurar qual é o indice na lista de jogadas possiveis que é igual à jogada   
        if [linha, coluna] == jogadas_possiveis[num]:
            grelha[linha - 1][coluna - 1] = jogador # Vai transformar o sitio da jogada numa peça do jogador
            virar = pecas_a_conquistar[num]         # E vai buscar a lista de peças a virar, armazenada no mesmo indice da lista a_conquistar

            for peca in range(len(virar)): # Ciclo para virar as peças
                linha_conquistada  = virar[peca][0] 
                coluna_conquistada = virar[peca][1]
                grelha[linha_conquistada - 1][coluna_conquistada - 1] = jogador # Mudança da peça

            jogo[0] = grelha # Inicio da rearmazenação
            jogo[1] = get_outro_jogador(jogador) # Suposto jogador seguinte
            proximo = reversi_proximo_a_jogar(jogo) # Verificar se pode realmente jogar
            proximo_a_jogar = proximo[0] # Ver quem é realmente o próximo a jogar

            jogada                   = is_valida(grelha, proximo_a_jogar) # tuplo com 2 listas: novas posições válidas para o
                                                                          # próximo jogador, e lista de peças a conquistar
            novas_jogadas            = jogada[0] # divisão do tuplo, para faciitar acesso
            novas_pecas_a_conquistar = jogada[1]
            jogo_atualizado = [grelha, proximo_a_jogar, novas_jogadas, novas_pecas_a_conquistar] # Atualização do jogo
        
            return jogo_atualizado # e continuação do mesmo!
    return jogo
