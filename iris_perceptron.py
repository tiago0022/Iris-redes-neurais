from file_read import readFile
from perceptron import perceptronTrain
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

data = readFile(filePath)
trainingData = data[0]
testData = data[1]

weigth = perceptronTrain(maxEpoch, learningRate, trainingData)
print('\nBias B + pesos W finais:\n')
print(weigth)
