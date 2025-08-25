def somar(a, b):
    """
    Esta função retorna a soma de dois números.
    """
    return a + b

def subtrair(a, b):
    """
    Esta função retorna a subtração de dois números.
    """
    return a - b

def multiplicar(a, b):
    """
    Esta função retorna a multiplicação de dois números.
    """
    return a * b
def dividir(a, b):
    """
    Esta função retorna a divisão de dois números.
    """
    if b == 0:
        return None
    return a / b
def potencia(a, b):
    """
    Esta função retorna a potência de um número elevado a outro.
    """
    return a ** b
def raiz_quadrada(a):
    """
    Esta função retorna a raiz quadrada de um número.
    """
    if a < 0:
        return None
    return a ** 0.5
def fatorial(n):
    """
    Esta função retorna o fatorial de um número.
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
def media(lista):
    """
    Esta função retorna a média de uma lista de números.
    """
    if not lista:
        return None
    return sum(lista) / len(lista)
def maximo(lista):
    """
    Esta função retorna o maior número de uma lista.
    """
    if not lista:
        return None
    return max(lista)
def minimo(lista):
    """
    Esta função retorna o menor número de uma lista.
    """
    if not lista:
        return None
    return min(lista)
def modulo(a, b):
    """
    Esta função retorna o módulo (resto da divisão) de dois números.
    """
    if b == 0:
        return None
    return a % b