num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print('Valores Digitados invalidos!!!')
