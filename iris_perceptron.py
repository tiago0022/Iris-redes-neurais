from file_read import readFile
from perceptron import perceptronTrain, perceptronTest
from iris_sample import Sample
import sys

functionAct = 'd'  # Argumento 1: função de ativação
if(len(sys.argv) > 1 and sys.argv[1]):
    functionAct = sys.argv[1]

maxEpoch = 25  # Argumento 2: máximo de épocas
if(len(sys.argv) > 2 and sys.argv[2]):
    maxEpoch = int(sys.argv[2])

learningRate = 0.1  # Argumento 3: taxa de aprendizagem
if(len(sys.argv) > 3 and sys.argv[3]):
    learningRate = float(sys.argv[3])

filePath = 'iris.data'  # Argumento 4: arquivo fonte
if(len(sys.argv) > 4 and sys.argv[4]):
    filePath = sys.argv[4]

# Leitura do arquivo
data = readFile(filePath)
trainingData = data[0]
testData = data[1]

# Treinamento
weigth = perceptronTrain(functionAct, maxEpoch, learningRate, trainingData)

# Teste
perceptronTest(functionAct, weigth[0], weigth[1], testData)
