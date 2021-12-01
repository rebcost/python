# Campo das importacoes
from art import header,vs
from game_data import data
import random
from os import system
# --- FIM ---

# Declaracoes de Funcoes
def informacoes_formatada(comparacao):
    """ Exibe na tela os dados de maneira formatada"""
    comparacao_nome = comparacao["name"]
    comparacao_descricao = comparacao["description"]
    comparacao_pais = comparacao["country"]

    return f"{comparacao_nome}, {comparacao_descricao}, do {comparacao_pais}"

def checar_resposta(resporta,a_seguidores,b_seguidores):
    """ Condicao para verificar a resposta do usuario    """
    if a_seguidores > b_seguidores:
        return resporta == "a"
    else:
        return resporta == "b"



# --- FIM ---


# ----- Programa Principal ------

# Importar a logo
print(header)

pontos = 0
deve_continuar = True
comparacao_b = random.choice(data) # Aqui vai gerar a primeira escolha aleatoria que vai ser passada para a variavel comparacao_a

while deve_continuar:

    # Gerar uma escolha aleatoria a partir do game_data
    # Logica para que a resposta que esta na variavel b passe para a variavel A
    comparacao_a = comparacao_b
    comparacao_b = random.choice(data) # Aqui comparacao_b vai receber um novo valor

    if comparacao_a == comparacao_b:
        comparacao_b = random.choice(data)

    #Formatar como as informaçoes são exibidas [Criada por meio de uma funcao]
    print(f"comparacaoA: {informacoes_formatada(comparacao_a)}")
    print(vs)
    print(f"comparacaoB: {informacoes_formatada(comparacao_b)}")

    # Perguntar ao usuario a resposta
    resposta = input("Quem tem mais seguidores? Escolha 'A' ou 'B': ").lower()


    # Checar se as respostas estao corretas
    ## Obter o numero de seguidores
    a_seguidores = comparacao_a["follower_count"]
    b_seguidores = comparacao_b["follower_count"]
    ## Usar a condiçao if para para obter a resposta correta
    esta_correto = checar_resposta(resposta,a_seguidores,b_seguidores)
    # Limpar a tela depois de cada rodada
    system("clear")
    print(header)

    if esta_correto:
        # Armazenar a pontuação
        pontos += 1
        print(f"Voce esta indo bem 😁. Pontuação: {pontos}")

    else:
        deve_continuar = False
        print(f"Sinto Muito, voce errou 😢. Pontuacao Final: {pontos}")
        



# ----- FIM ------