# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
# nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa
# não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

print('Bem vindo a calculadora de Equação')
a = float(input('Digite o valor para A: '))
b = float(input('Digite o valor para B: '))
c = float(input('Digite o valor para C: '))
D = (b**2 - 4*a*c)
x1 = (-b + D**(1/2)) / (2*a)
x2 = (-b - D**(1/2)) / (2*a)

if a == 0:
    print('A equação não é do 2º GRAU')
elif D < 0:
    print('A equação não possui raízes reais')
elif D == 0:
    print(f'A equação possui apenas uma raiz real'
          f'Raíz real: {x1:.2f}')
elif D > 0:
    print(f'A equação possui duas raízes reais:{x1}\n{x2:.2f}')