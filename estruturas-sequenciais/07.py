'''

Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

print('Olá Bem seja vindo!!')
__hora_semanais = (int(input('Quanto você ganha por hora?: ')))
__horas_trabalhadas = int(input('Quantas horas você trabalhou no mês? '))
__resultado = __hora_semanais * __horas_trabalhadas

print(f'O total do seu sálario baseado nos dados informados: {__resultado}')