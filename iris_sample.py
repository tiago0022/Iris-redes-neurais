SETOSA_NAME = 'Iris-setosa'
VERSICOLOR_NAME = 'Iris-versicolor'
VIRGINICA_NAME = 'Iris-virginica'

SETOSA_VECTOR = [0, 0, 1]
VERSICOLOR_VECTOR = [0, 1, 0]
VIRGINICA_VECTOR = [1, 0, 0]


class Sample:  # classe que representa uma linha da base de dados

    def __init__(self, line):

        values = line[:-1].split(',')

        self.attributeListX = []  # vetor de entrada X

        self.attributeListX.append(float(values[0]))  # sepalLength
        self.attributeListX.append(float(values[1]))  # sepalWidth
        self.attributeListX.append(float(values[2]))  # petalLength
        self.attributeListX.append(float(values[3]))  # petalWidth
        self.className = values[4]  # nome da classe

        # mapeia a classe de acordo com seu vetor:
        if(self.className == SETOSA_NAME):
            self.classY = SETOSA_VECTOR
        if(self.className == VERSICOLOR_NAME):
            self.classY = VERSICOLOR_VECTOR
        if(self.className == VIRGINICA_NAME):
            self.classY = VIRGINICA_VECTOR
