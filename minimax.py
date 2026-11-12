from functools import lru_cache

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


# Maximizando indica de quem é a vez de jogar
# True = X, False = O
@lru_cache(maxsize=None)
def minimax(tabuleiro, maximizando):

    tabuleiro = list(tabuleiro)
    resultado = verificarVencedor(tabuleiro)

    if resultado == "X":
        return 1

    if resultado == "O":
        return -1

    if resultado == "Empate":
        return 0

    if maximizando: # Vez do X jogar
        melhorPontuacao = float("-inf")

        for jogada in jogadasDisponiveis(tabuleiro):
            tabuleiro[jogada] = "X"
            pontuacao = minimax(tuple(tabuleiro), False)
            tabuleiro[jogada] = ""

            melhorPontuacao = max(melhorPontuacao, pontuacao)

        return melhorPontuacao

    else: # Vez do O jogar
        melhorPontuacao = float("inf")

        for jogada in jogadasDisponiveis(tabuleiro):
            tabuleiro[jogada] = "O"
            pontuacao = minimax(tuple(tabuleiro), True)
            tabuleiro[jogada] = ""

            melhorPontuacao = min(melhorPontuacao, pontuacao)

        return melhorPontuacao


def melhorJogada(tabuleiro, jogador):

    if jogador == "X":
        melhorPontuacao = float("-inf")
        maximizando = False
    else:
        melhorPontuacao = float("inf")
        maximizando = True

    melhorMovimento = None

    for jogada in jogadasDisponiveis(tabuleiro):
        tabuleiro[jogada] = jogador
        pontuacao = minimax(tuple(tabuleiro), maximizando)
        tabuleiro[jogada] = ""

        if jogador == "X":
            if pontuacao > melhorPontuacao:
                melhorPontuacao = pontuacao
                melhorMovimento = jogada

        else:
            if pontuacao < melhorPontuacao:
                melhorPontuacao = pontuacao
                melhorMovimento = jogada

    return melhorMovimento


if __name__ == "__main__":

    tabuleiro = [
        "X", "X", "",
        "O", "O", "",
        "", "", ""
    ]

    resultado = verificarVencedor(tabuleiro)
    jogadas = jogadasDisponiveis(tabuleiro)
    pontuacao = minimax(tuple(tabuleiro), True)

    print("Melhor pontuacao:", pontuacao)
    print("Jogadas disponíveis:", jogadas)
    print("Resultado:", resultado)

    tabuleiroX = [
        "X", "X", "",
        "O", "O", "",
        "", "", ""
    ]

    jogadaX = melhorJogada(tabuleiroX, "X")
    print("Melhor jogada do X:", jogadaX)

    tabuleiroO = [
        "X", "X", "",
        "O", "", "",
        "", "", ""
    ]

    jogadaO = melhorJogada(tabuleiroO, "O")
    print("Melhor jogada do O:", jogadaO)
