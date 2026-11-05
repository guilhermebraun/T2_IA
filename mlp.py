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
        self.pesosSaida = np.random.uniform(-1, 1, (self.qtEntradas, self.qtSaidas))
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
        somaOculta = np.dot(entrada, self.pesosOcultos) + self.biasOcultos
        saidaOculta = self.sigmoide(somaOculta)

        # Calcular a camada de saída
        somaSaida = np.dot(saidaOculta, self.pesosSaida) + self.biasSaida

        return somaSaida
