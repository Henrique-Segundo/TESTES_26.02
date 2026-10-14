#Teste da atividade pratica Caça as Bruxas, adaptado para python com o uso de IA, ChatGPT, e adaptado manualmente 

def potencial_teste(base,expoente):

    if expoente <= 0:
        potencial = 0 - expoente
    else:
        potencial = expoente

    resultado = 1

    while potencial != 0:
        resultado = resultado * base
        potencial = potencial - 1

    if expoente < 0 and base != 0:
        resultado = 1 / resultado
    else:
        if base == 0:
            raise ValueError("A potência é um valor finito")

    print("A potência é", resultado)
    return resultado


def busca_binaria(array, valor):
    inicio = 0
    fim = len(array) - 1
    retorno = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if array[meio] == valor:
            retorno = meio
            fim = -1
        elif valor > array[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1

    return retorno

def obter_aprovacao(num_faltas, qtd_creditos, nota_total, nota_prova_final):
    porcentagem_presenca = None

    if num_faltas is not None:
        porcentagem_presenca = num_faltas * 100 / qtd_creditos * 36

    if nota_total >= 60:
        return True
    else:
        if nota_prova_final >= 60:
            return True
        else:
            return False

def fib(n):
    a = 1
    b = 1
    c = 2

    if 0 == n:
        return 0

    if n < 3:
        return 1

    while n > 2:
        n -= 1
        c = a + b
        a = b
        b = c

    return c


def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr

def q6(x,y):

    if y < 0:
        p = 0 - y
    else:
        p = y

    z = 1.0

    while p != 0:
        z = z * x
        p = p - 1

    if y < 0:
        z = 1 / z

    return z