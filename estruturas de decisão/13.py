# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.)
# se digitar outro valor deve aparecer valor inválido.
numero = int(input('Digite um número de 1 á 7: '))

if numero == 1:
    print('Segunda-Feira')
elif numero == 2:
    print('Terça-Feira')
elif numero == 3:
    print('Quarta-Feira')
elif numero == 4:
    print('Quinta-Feira')
elif numero == 5:
    print('Sexta-Feira')
elif numero == 6:
    print('Sábado')
elif numero == 7:
    print('Domingo')
else:
    print('Valor digitado inválido')


