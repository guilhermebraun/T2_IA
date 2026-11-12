import numpy as np

class MLP:
    def __init__(self, qtdNeuroniosOcultos=10):
        # qtd de neurônios
        self.qtEntradas = 9
        self.qtNeuroniosOcultos = qtdNeuroniosOcultos
        self.qtSaidas = 9

        # pesos da camada oculta
        self.pesosOcultos = np.random.uniform(-1, 1, (self.qtEntradas, self.qtNeuroniosOcultos))
        # bias da camada oculta
        self.biasOculto = np.random.uniform(-1, 1, self.qtNeuroniosOcultos)
        # pesos da camada de saída
        self.pesosSaida = np.random.uniform(-1, 1, (self.qtNeuroniosOcultos, self.qtSaidas))
        # Bias da camada de saída
        self.biasSaida = np.random.uniform(-1, 1, self.qtSaidas)

    def sigmoide(self, x):
        return 1 / (1 + np.exp(-x))

    def propagar(self, tabuleiro):
        entrada = []
        for posicao in tabuleiro:
            if posicao == "X":
                entrada.append(1)
            elif posicao == "O":
                entrada.append(-1)
            else:
                entrada.append(0)

        entrada = np.array(entrada)

        # Calcular a camada oculta
        somaOculta = np.dot(entrada, self.pesosOcultos) + self.biasOculto
        saidaOculta = self.sigmoide(somaOculta)

        # Calcular a camada de saída
        somaSaida = np.dot(saidaOculta, self.pesosSaida) + self.biasSaida

        return somaSaida

    def indicarJogada(self, tabuleiro):
        saidas = self.propagar(tabuleiro)

        # Considera somente as posicoes vazias
        for i in range(len(tabuleiro)):
            if tabuleiro[i] != "":
                saidas[i] = float("-inf")

        melhorMovimento = np.argmax(saidas)
        return melhorMovimento


    def obterParametros(self):
        parametros = np.concatenate((
            self.pesosOcultos.flatten(),
            self.biasOculto.flatten(),
            self.pesosSaida.flatten(),
            self.biasSaida.flatten()
        ))

        return parametros

    def definirParametros(self, cromossomo):
        # Separar os parametros do cromossomo
        tamPesosOcultos = self.qtEntradas * self.qtNeuroniosOcultos
        tamBiasOculto = self.qtNeuroniosOcultos
        tamPesosSaida = self.qtNeuroniosOcultos * self.qtSaidas

        inicio = 0

        pesosOcultos = cromossomo[inicio:inicio + tamPesosOcultos]
        inicio += tamPesosOcultos
        biasOculto = cromossomo[inicio:inicio + tamBiasOculto]
        inicio += tamBiasOculto
        pesosSaida = cromossomo[inicio:inicio + tamPesosSaida]
        inicio += tamPesosSaida
        biasSaida = cromossomo[inicio:]

        # Reconstruir as matrizes e vetores
        self.pesosOcultos = pesosOcultos.reshape(
            self.qtEntradas,
            self.qtNeuroniosOcultos
        )

        self.biasOculto = biasOculto

        self.pesosSaida = pesosSaida.reshape(
            self.qtNeuroniosOcultos,
            self.qtSaidas
        )

        self.biasSaida = biasSaida


if __name__ == "__main__":
    # Criar a rede neural
    rede = MLP()

    cromossomo = rede.obterParametros()
    print("Quantidade de genes:", len(cromossomo))

    rede.definirParametros(cromossomo)

    novoCromossomo = rede.obterParametros()
    print("Parametros foram mantidos:", np.array_equal(cromossomo, novoCromossomo))

    tabuleiro = [
        "X", "O", "X",
        "",  "X", "",
        "O", "",  ""
    ]

    # Executar a propagação
    resultado = rede.propagar(tabuleiro)
    jogada = rede.indicarJogada(tabuleiro)

    print("Saídas da rede:")
    print(resultado)

    print("Quantidade de saídas:", len(resultado))
    print("Jogada indicada pela rede:", jogada)
