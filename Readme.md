# Aprendizado supervisionado
Este trabalho tem como objetivos:
- Implementação das seguintes funções de aprendizado de máquina em uma regressão linear, no arquivo "alegrete.py":
- - Erro médio quadrático.
- - Descida do gradiente.

- Treinamento de modelos de Redes Neurais Convolucionais (CNNs) para a classificação de imagens de datasets conhecidos (MNIST, CIFAR).

## Regressão linear
**Valores iniciais otimizados:**\
b      = -1\
w      = 1.5\
alpha  = 0.01\
n_iter = 1000\
EQM final: 8.53

**Valores iniciais aleatórios:**\
b      = 5\
w      = -2\
alpha  = 0.01\
n_iter = 1000\
EQM final: 9.452

## Redes neurais
### Análise dos datasets

**CIFAR-10**\
Classes = 10\
Amostras (train+test) = 50.000 + 10.000\
Tamanho das imagens = 32 x 32 x 3

**CIFAR-100**\
Classes = 100\
Amostras (train+test) = 50.000 + 10.000\
Tamanho das imagens = 32 x 32 x 3

**MNIST**\
Classes = 10\
Amostras (train+test) = 60.000 + 10.000\
Tamanho das imagens = 28 x 28 x 1

**FASHION_MNIST**\
Classes = 10\
Amostras (train+test) = 60.000 + 10.000\
Tamanho das imagens = 28 x 28 x 1

**Conclusões:**
- MNIST: Imagens com apenas um canal de cor (tons de cinza) são facilmente tratáveis com apenas 1 camada convolucional. Mesmo sem normalizar os pixels, utilizando os hiperparâmetros mais básicos, o modelo atingiu cerca de 95% de acurácia.
- CIFAR: As imagens em RGB necessitaram de mais camadas convolucionais com maiores strides para melhorar a acurácia. Além disso, a normalização dos dados, a substituição da função de ativação ReLu por GeLu/Elu, a função de perda *sparse* e a utilização de decaimento dos pesos melhorou o modelo sem aumentar tanto a complexidade computacional.

## Bibliotecas adicionais
Pandas (utilizado nas funções em alegrete.py)

## Créditos
[José](https://github.com/dev-joseh)\
[Gabriel](https://github.com/gabrielcarvalhoavila)
