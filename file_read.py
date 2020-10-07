from iris_sample import Sample
import random


def readFile(fileName: str):  # executa a leitura do arquivo e traduz para a entidade conhecida

    file = open(fileName, "r")

    trainingData = []
    testData = []

    i = 0
    for line in file:
        if ((i % 10) < 7):  # divide a base de dados em 70% dos dados para treinamento
            trainingData.append(Sample(line))
        else:  # e 30% dos dados para teste
            testData.append(Sample(line))
        i += 1

    # Embaralha as listas para que o algoritmo não vicie no tipo inicial
    random.shuffle(trainingData)
    random.shuffle(testData)

    # A variável data será retornada contendo o conjunto de testes e o conjunto de treinamento
    data = []
    data.append(trainingData)
    data.append(testData)

    file.close()

    return data
