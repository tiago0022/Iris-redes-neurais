from file_read import readFile
from perceptron import perceptronTrain, perceptronTest
from iris_sample import Sample
import sys

maxEpoch = 25  # Argumento 1: máximo de épocas
if(len(sys.argv) > 1 and sys.argv[1]):
    maxEpoch = int(sys.argv[1])

learningRate = 0.1  # Argumento 2: taxa de aprendizagem
if(len(sys.argv) > 2 and sys.argv[2]):
    learningRate = float(sys.argv[2])

filePath = 'iris.data'  # Argumento 3: arquivo fonte
if(len(sys.argv) > 3 and sys.argv[3]):
    filePath = sys.argv[3]

# Leitura do arquivo
data = readFile(filePath)
trainingData = data[0]
testData = data[1]

# Treinamento
weigth = perceptronTrain(maxEpoch, learningRate, trainingData)

# Teste
perceptronTest(weigth[0], weigth[1], testData)
