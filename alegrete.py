import numpy as np

def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    mse = 0
    n = int(data.size/2)
    for i in range(n):
        mse += (data[i][1]-(data[i][0]*w+b))**2 # Y - y

    return mse/n

def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """

    base = [b,w]
    options = [(b+alpha,w),
              (b+alpha,w+alpha),
              (b+alpha,w-alpha),
              (b-alpha,w),
              (b-alpha,w+alpha),
              (b-alpha,w-alpha),
              (b,w+alpha),
              (b,w-alpha)]

    for i in range(8):
        if compute_mse(base[0],base[1],data) > compute_mse(options[i][0],options[i][1],data):
            base[0] = options[i][0]
            base[1] = options[i][1]

    return base

def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    resultados = [[],[]]

    for i in range(num_iterations):
        b,w=step_gradient(b,w,data,alpha)
        resultados[0].append(b)
        resultados[1].append(w)

    return resultados

"""
# Testes
b=3
w=3
dados = np.array([[0,1,2,3,4,5,6], [1,3,5,7,9,11,13]])
alpha=0.01

# print(compute_mse(b,w,dados))

resultados_fit = fit(dados,b,w,alpha,1000)
print(resultados_fit[0][-1])
print(resultados_fit[1][-1])
"""