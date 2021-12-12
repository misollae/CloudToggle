
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



# escolhas do jogador 
simbolo_escolhido = None
ordem_escolhida   = None
# variáveisd auxiliares
simbolo_primeiro_a_jogar = None
simbolo_segundo_a_jogar  = None





def simbolo_valido(simbolo):

    if simbolo == 'O' or simbolo == 'X' or simbolo == '':
        return True
    else:
        return False




    
def ordem_valida(simbolo):

    if simbolo == '1' or simbolo == '2' or simbolo == '':
        return True
    else:
        return False


    
    

def converte_valor(valor):

    #return str(valor)

    if valor == 0:
        return ' '
    if valor == 1:
        return simbolo_primeiro_a_jogar
    if valor == 2:
        return simbolo_segundo_a_jogar



    

def get_valor_string(jogo, linha, coluna):

    if reversi_jogada_possivel(jogo, linha, coluna):
        return '?'
    else:
        return converte_valor(reversi_valor(jogo, linha, coluna))



    

def print_pontos(jogo):        

    pontos = reversi_pontuacao(jogo)

    print('pontos ' + converte_valor(1) + ' = ' + str(pontos[0]) + ' pontos '
          + converte_valor(2) + ' = ' + str(pontos[1]) )


    
    
    
def print_grelha(jogo):

    linha_horizontal = '---|-------------------------------|'
    
    print('   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |')
    print(linha_horizontal)
    
    for l in range(8):
        linha = ' ' + str(l+1) + ' | '
        for c in range(8):
            valor_string = get_valor_string(jogo, l+1, c+1)
            linha = linha + valor_string + ' | '
        print(linha)
        print(linha_horizontal)
        

        
        

def mensagem_passou(jogador):

    print('Quem joga com ' + converte_valor(jogador)
          + ' não tinha como jogar. PASSOU!!!')



    
    
def mensagem_proximo_a_jogar(jogador):

    print('PRÓXIMO A JOGAR: ' + converte_valor(jogador))



    
    
def print_vencedor(jogo):

    pontos = reversi_pontuacao(jogo)

    if pontos[0] > pontos[1]:
        print('jogador ' + converte_valor(1) + ' GANHOU!!!')
    elif pontos[0] < pontos[1]:
        print('jogador ' + converte_valor(2) + ' GANHOU!!!')
    else:
        print('EMPATE!!!')


        
        

def jogada_jogador(jogo):

    jogada = input('insira a sua jogada: ')

    if jogada != '':

        linha  = int(jogada[0])
        coluna = int(jogada[1])

    else:

        (linha, coluna) = jogada_agente(jogo)
        print('jogada agente: ' + str(linha) + str(coluna))

    return (linha, coluna)




    
def jogada_computador(jogo):

    (linha, coluna) = jogada_agente(jogo)
    
    print('jogada computador: ' + str(linha) + str(coluna))

    return (linha, coluna)




    
welcome = '''

ISEL - Reversi!

Nesta versão do Reversi joga-se contra o computador.

Para jogar insira o número da linha seguido do número da coluna (sem
espaço) seguido da tecla enter.

Pode também jogar usando o agente, carregando apenas a tecla enter.

'''

escolha_simbolo = '''Que jogar com O ou com X?
Insira um O (o maiúsculo) ou um X (x maiúsculo), seguido da tecla enter.
Se carregar diretamente na tecla enter, jogará com o O (valor pré-definido).
A sua escolha: '''

erro_escolha_simbolo = '''Não inseriu nem um O nem um X, seguido da tecla enter.
Tente outra vez.'''

escolha_ordem = '''Que ser o primeiro ou o segundo a jogar?
Insira um 1, seguido da tecla entre, para ser o primeiro a jogar
ou um 2, seguido da tecla enter, para ser o segundo a jogar.
Se carregar diretamente na tecla enter, jogará em primeiro lugar (valor pré-definido).
A sua escolha: '''

erro_escolha_ordem = '''Não inseriu nem um 1 nem um 2, seguido da tecla enter.
Tente outra vez.'''


print(welcome)

simbolo_escolhido = input(escolha_simbolo)
while not simbolo_valido(simbolo_escolhido):
    print(erro_escolha_simbolo)
    simbolo_escolhido = input(escolha_simbolo)

# valor pré-definido
if simbolo_escolhido == '':
    simbolo_escolhido = 'O'
    
ordem_escolhida = input(escolha_ordem)
while not ordem_valida(ordem_escolhida):
    print(erro_escolha_ordem)
    ordem_escolhida = input(escolha_ordem)

# valor pré-definido
if ordem_escolhida == '':
    ordem_escolhida = '1'

print(simbolo_escolhido)
print(ordem_escolhida)

if ordem_escolhida == '1':
    if simbolo_escolhido == 'O':
        simbolo_primeiro_a_jogar = 'O'
        simbolo_segundo_a_jogar  = 'X'
    else:
        simbolo_primeiro_a_jogar = 'X'
        simbolo_segundo_a_jogar  = 'O'
else:
    if simbolo_escolhido == 'O':
        simbolo_primeiro_a_jogar = 'X'
        simbolo_segundo_a_jogar  = 'O'
    else:
        simbolo_primeiro_a_jogar = 'O'
        simbolo_segundo_a_jogar  = 'X'

print('simbolo_primeiro_a_jogar = ' + simbolo_primeiro_a_jogar)
print('simbolo_segundo_a_jogar  = ' + simbolo_segundo_a_jogar)

# só para testes - as próximas duas linhas permitem ver diretamente o
# que está na grelha

#simbolo_primeiro_a_jogar = '1'
#simbolo_segundo_a_jogar  = '2'

jogo = reversi_novo_jogo()

while not reversi_fim_jogo(jogo):

    print_pontos(jogo)
    print_grelha(jogo)

    (proximo_a_jogar, jogador_que_passou) = reversi_proximo_a_jogar(jogo)

    if jogador_que_passou != None:
        mensagem_passou(jogador_que_passou)

    mensagem_proximo_a_jogar(proximo_a_jogar)

    if proximo_a_jogar == int(ordem_escolhida):

        # para testes dá muito jeito pôr o computador a jogar com o computador
        # comentar a próxima linha e descomentar a seguinte
        (linha, coluna) = jogada_jogador(jogo)
        #(linha, coluna) = jogada_computador(jogo)

    else:

        (linha, coluna) = jogada_computador(jogo)
    
    jogo = reversi_jogar(jogo, linha, coluna)

print_pontos(jogo)    
print_grelha(jogo)
print_vencedor(jogo)

