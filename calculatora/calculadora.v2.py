from funcoes_calculadora import *

saida = ''

while saida not in ('n', 'nao', 'não'):
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        continue    
    oper = input("Qual a operação desejada? [+, -, x, / ou nome]: ").strip().lower()
    resultado = calculadora(num1, num2, oper)
    print(f'Resultado da operação: {resultado}')
    saida = input('Deseja continuar? [S/N] ').strip().lower()
    while saida not in ('s', 'n', 'sim', 'não', 'nao'):
        saida = input('Digite "S" para continuar ou digite "N" para saír. Deseja continuar? [S/N] ').strip().lower()

