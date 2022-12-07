# Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(f'{n1}, {n2}, {n3}')
    else:
        print(f'{n1}, {n3}, {n2}')
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print(f'{n2}, {n1}, {n3}')
    else:
        print(f'{n2}, {n3}, {n1}')
if n3 > n2 and n3 > n1:
    if n2 > n1:
        print(f'{n3}, {n2}, {n1}')
    else:
        print(f'{n3}, {n1}, {n2}')