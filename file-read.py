file = open("iris.data", "r")

trainingData = []
testData = []

i = 0
for line in file:
    if ((i % 10) < 7):  # divide a base de dados em 70% dos dados para treinamento
        trainingData.append(line)
    else:  # e 30% dos dados para teste
        testData.append(line)
    i += 1

data = []  # a variável data será retornada contendo o conjunto de testes e o conjunto de treinamento
data.append(trainingData)
data.append(testData)

print(data[0])
print()
print(data[1])

file.close()
