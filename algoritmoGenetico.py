import numpy as np
from mlp import MLP

tamPopulacao = 100

redeReferencia = MLP()
qtGenes = len(redeReferencia.obterParametros())

# Gera um individuo com 199 parametros aleatorios
def gerarIndividuo():
    individuo = np.random.uniform(-1, 1, qtGenes)

    return individuo

# Gera a populacao inicial
def gerarPopulacao():
    populacao = []
    for i in range(tamPopulacao):
        individuo = gerarIndividuo()
        populacao.append(individuo)

    return populacao


if __name__ == "__main__":

    populacao = gerarPopulacao()

    print("Quantidade de individuos:", len(populacao))
    print("Quantidade de genes por individuo:", len(populacao[0]))

    print("\nPrimeiro individuo (5 primeiros genes):")
    print(populacao[0][:5])
    
    print("\nTodos os individuos possuem 199 genes:",
      all(len(individuo) == qtGenes for individuo in populacao))
