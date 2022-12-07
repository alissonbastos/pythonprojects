'''

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

h = float(input('Digite sua altura: '))

homens = (72.7*h) - 58
mulheres = (62.1*h) - 44.7

print(f'Se você é um homem, seu peso ideal seria: {homens}')
print(f'Se você é uma mulher, seu peso ideal seria: {mulheres}')