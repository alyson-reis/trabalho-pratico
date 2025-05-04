def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multipliacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

def calculadora(n1, n2, op):
    if op in ("+", "soma"):
        return adicao(n1, n2)
    elif op in ("-", "subtracao", "subtração"):
        return subtracao(n1, n2)
    elif op in ("x", "*", "multiplicacao", "multiplicação"):
        return multipliacao(n1, n2)
    elif op in ("/", "divisao", "divisão"):
        return divisao(n1, n2)
    else:
        return 'Operação inválida'
def encerramento():
    print('Fim do processo')
