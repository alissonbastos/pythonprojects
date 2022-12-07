'''Faça um Programa que leia três números e mostre o maior deles.'''

num1 = int(input('Digite o 1º valor: '))
num2 = int(input('Digite o 1º valor: '))
num3 = int(input('Digite o 1º valor: '))

if num1 >= num2 and num1 >= num3:
    maior = num1
    print(f'O maior valor digitado é {maior}')
elif num2 >= num2 >= num3:
    maior = num2
    print(f'O maior valor digitado é {maior}')
elif num3 >= num1 and num3 >= num2:
    maior = num3
    print(f'O maior valor é {maior}')
else:
    print('Não encontrado')