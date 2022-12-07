#   Faça um programa que pergunte o preço de três produtos e informe qual produto você
#   deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input('Digite o preço do 1º produto: '))
p2 = float(input('Digite o preço do 1º produto: '))
p3 = float(input('Digite o preço do 1º produto: '))

if p1 < p2 and p1 < p3:
    print(f'O produto mais em conta é R$ {p1}')
elif p2 < p1 and p2 < p3:
    print(f'O produto mais em conta é R$ {p2}')
elif p3 < p1 and p3 < p2:
    print(f'O produto mais em conta é R$ {p3}')
