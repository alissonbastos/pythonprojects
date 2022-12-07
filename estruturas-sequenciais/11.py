X = int(input('Digite um número inteiro:\n>>>'))
Y = int(input('Digite outro número inteiro:\n>>>'))
Z = float(input('Digite um número real:\n>>>'))
'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''
dobro = X ** 2 + (Y / 2)
print(f'O produto do dobro do primeiro  + metade do segundo número: {dobro} ')
triplo = Y * 3 + Z
print(f'O triplo do primeiro mais soma com o terceiro: {triplo}')
terceiro = Z ** 3
print(f'Terceiro elevado ao cubo: {terceiro}')