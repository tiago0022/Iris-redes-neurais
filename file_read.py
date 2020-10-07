from iris_sample import Sample


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

    data = []  # a variável data será retornada contendo o conjunto de testes e o conjunto de treinamento
    data.append(trainingData)
    data.append(testData)

    file.close()

    # for x in trainingData:
    #     print(x.attributeListX)

    return data
