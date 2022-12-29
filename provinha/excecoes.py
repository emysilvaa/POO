try:
    n1 = int(input('número 1: '))
    n2 = int(input('numero 2: '))
    soma = n1+n2
    print(soma)
except ValueError as erro:
    print('Você digitou um valor inválido')

