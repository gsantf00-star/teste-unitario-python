
# calculadora.py

def calcular_media(lista):
    if not lista:
        raise ValueError("A lista não pode ser vazia")
    return sum(lista) / len(lista)

def potencia(a,b):
    """Retorna a potencia de dois números."""
    return a ** b

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de dois números.

    Se o segundo número for zero, o Python irá gerar um erro.
    """
    return a / b
