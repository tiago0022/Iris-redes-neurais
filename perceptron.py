from iris_sample import Sample
import random
import numpy as np


def perceptronTrain(maxEpoch, learningRate, sampleList):

    classCount = len(sampleList[0].classY)
    attributeCount = len(sampleList[0].attributeListX)

    weigthMatrix = initMatrix(attributeCount, classCount)
    biasList = initVector(classCount)

    epochT = 1
    cumulativeError = 1

    # executa o treinamento até que o erro seja 0 ou chegue ao máximo de épocas
    while(epochT < maxEpoch and cumulativeError > 0):
        cumulativeError = 0
        for sample in sampleList:
            print('Vetor de entrada X:')
            print(sample.attributeListX)
            print('\nMatriz de pesos W:')
            print(weigthMatrix)
            print('\nVetor de bias B:')
            print(biasList)
            print('\nMultiplicação W * X:')
            result = np.matmul(weigthMatrix, np.transpose(sample.attributeListX))
            print(result)
            print('\n===============\n')
        # print(weigthList)
        # print(sample.attributeListX)
        # print(biasList)
        # print()


def initVector(size: int):  # inicializa um vetor de valores entre -1 e 1
    vector = []
    for _ in range(size):
        vector.append(round(random.uniform(-1, 1), 1))
    return np.array(vector)


def initMatrix(width: int, height: int):  # inicializa uma matriz de valores entre -1 e 1
    matrix = []
    for _ in range(height):
        matrix.append(initVector(width))
    return np.array(matrix)
