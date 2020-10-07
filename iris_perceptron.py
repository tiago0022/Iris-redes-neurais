from file_read import readFile
from perceptron import perceptronTrain
from iris_sample import Sample

data = readFile('iris.data')
trainingData = data[0]
testData = data[1]

perceptronTrain(5, 0.3, trainingData)
