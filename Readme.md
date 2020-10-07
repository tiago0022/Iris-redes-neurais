Iris - redes neurais Lab. IA 2020/1

Para executar o treinamento da rede:

python3 iris_perceptron.py [funcao_ativacao] [epocas] [taxa_aprendizado] [nome_arquivo]

- [função ativação]: degrau: ‘d’ / sigmoidal: ‘s’  →  padrão = degrau
- [épocas]: máximo de épocas do algoritmo  → padrão = 25
- [taxa de aprendizado]:  padrão = 0.1
- [nome do arquivo]: nome do arquivo com os dados para leitura, é necessário que o arquivo esteja no formato correto  →  padrão = ‘iris.data’

Ao executar o algoritmo, o terminal irá exibir a matriz de pesos W e o bias B obtidos no final de cada época, além de seu erro acumulado. E ao fim do treinamento, irá executar o teste e verificar a acurácia obtida
