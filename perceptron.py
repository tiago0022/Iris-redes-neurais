from iris_sample import Sample
import random
import numpy as np


def perceptronTrain(maxEpoch, learningRate, sampleList):

    printSampleIteration = True

    classCount = len(sampleList[0].classY)
    attributeCount = len(sampleList[0].attributeListX)

    weigthW = initMatrix(attributeCount, classCount)  # matriz de pesos W
    biasB = np.matrix(initVector(classCount)).transpose()  # vetor de bias

    epochT = 1
    cumulativeError = 1

    # executa o treinamento até que o erro seja 0 ou chegue ao máximo de épocas
    while(epochT <= maxEpoch and cumulativeError > 0):
        print('\nÉpoca', epochT, ':')
        print('\nMatriz de pesos W:')
        print(weigthW)
        print('\nBias B:')
        print(biasB)
        cumulativeError = 0
        # na mesma época, obtem o resultado de cada amostra
        for sample in sampleList:
            # Atributos da amostra de entrada X
            inputX = np.matrix(sample.attributeListX).transpose()
            # Cálculo W * X + B
            WXB = np.matmul(weigthW, inputX) + biasB
            # Resultado esperado D
            labelD = np.matrix(sample.classY).transpose()
            # Resultado obtido Y por meio da função de ativação degrau f
            outputY = stepActivation(WXB)
            # Erro obtido comparando D e Y
            errorE = labelD - outputY
            # Cálculo de (alpha * E * X) que será a matriz de ajustes aplicados à W
            alphaEX = np.matmul(learningRate * errorE, inputX.transpose())
            # Cálculo dos novos pesos W
            weigthW = weigthW + alphaEX
            # Cálculo do novo bias B
            biasB = biasB + learningRate * errorE
            # Erro escalar acumulado |E| nesta época
            cumulativeError = cumulativeError + getScalarError(errorE)
            # Na primeira iteração, exibe o algoritmo detalhadamente
            if(printSampleIteration):
                printSampleIteration = False
                print('\nAmostra X:')
                print(inputX)
                print('\nSoma WX + B:')
                print(WXB)
                print('\nRótulo D esperado:')
                print(labelD)
                print('\nSaída Y da rede:')
                print(outputY)
                print('\nErro E para a amostra:')
                print(errorE)
                print('\nModificação alpha*E*X em W:')
                print(alphaEX)
                print('\nNova matriz de pesos W:')
                print(weigthW)
                print('\nNovo vetor bias B:')
                print(biasB)
                print('\nCálculo do erro acumulado escalar |E|:')
                print(cumulativeError)
                print('\n===============')
        print('\nErro acumulado |E|:', cumulativeError)
        print('\n============== FIM ÉPOCA', epochT, '==============')
        epochT += 1
    return np.hstack((biasB, weigthW))


def initVector(size: int):  # inicializa um vetor de valores entre -0.9 e 0.9
    vector = []
    for _ in range(size):
        vector.append(round(random.uniform(-0.9, 0.9), 1))
    return np.array(vector)


def initMatrix(width: int, height: int):  # inicializa uma matriz de valores entre -0.9 e 0.9
    matrix = []
    for _ in range(height):
        matrix.append(initVector(width))
    return np.matrix(matrix)


def stepActivation(vector):  # função de ativação degrau
    stepVector = []
    for element in vector:
        if(element >= 0):
            stepVector.append(1)
        else:
            stepVector.append(0)
    return np.matrix(stepVector).transpose()


def getScalarError(numberList):  # função para cálculo do erro acumulado escalar
    error = 0
    for line in numberList.tolist():
        for number in line:
            error += number * number
    return error
