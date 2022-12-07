# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

if n1 > n2 and n1 > n3:
    if n2 < n3:
        print(f'O número {n1} é o maior e o {n2} é o menor')
    else:
        print(f'O número {n1} é o maior e o {n3} é o menor')
if n2 > n1 and n2 > n3:
    if n3 < n1:
        print(f'O número {n2} é o maior e o {n3} é o menor')
    else:
        print(f'O número {n2} é o maior e o {n1} é o menor')
if n3 > n1 and n3 > n2:
    if n1 < n2:
        print(f'O número {n3} é o maior e o {n1} é o menor')
    else:
        print(f'O número {n1} é o maior e o {n2} é o menor')
