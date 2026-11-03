
def verificarVencedor(tabuleiro):

    combinacoes = [ #Vitórias
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinacoes:

        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != "":
            return tabuleiro[a]

    if "" not in tabuleiro:
        return "Empate"

    return None


def jogadasDisponiveis(tabuleiro):
    jogadas = []
    for i in range(len(tabuleiro)):
        if tabuleiro[i] == "":
            jogadas.append(i)
    
    return jogadas


def minimax(tabuleiro, maximizando):
    resultado = verificarVencedor(tabuleiro)
    if resultado == "X":
        return 1
    if resultado == "O":
        return -1
    if resultado == "Empate":
        return 0
    
    if maximizando:
        melhorPontuacao = float("-inf")
        for jogada in jogadasDisponiveis(tabuleiro):
            tabuleiro[jogada] = "X"
            pontuacao = minimax(tabuleiro, False)
            tabuleiro[jogada] = ""
            melhorPontuacao = max(melhorPontuacao, pontuacao)

        return melhorPontuacao

    else:
        melhorPontuacao = float("inf")
        for jogada in jogadasDisponiveis(tabuleiro):
            tabuleiro[jogada] = "O"
            pontuacao = minimax(tabuleiro, True)
            tabuleiro[jogada] = ""
            melhorPontuacao = min(melhorPontuacao, pontuacao)

        return melhorPontuacao



tabuleiro = [
    "X", "X", "",
    "O", "O", "",
    "", "", ""
    ]

resultado = verificarVencedor(tabuleiro)
jogadas = jogadasDisponiveis(tabuleiro)
pontuacao = minimax(tabuleiro, True)

print("Melhor pontuacao:", pontuacao)
print("Jogadas disponíveis: ", jogadas)
print("Resultado:", resultado)
