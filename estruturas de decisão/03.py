'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

letra = input('Digite uma Letra: ')
if letra == 'M' and 'm':
    print('Sexo Masculino')
elif letra == 'F' and 'f':
    print('Sexo Feminino')
else:
    print('Sexo Inválido')