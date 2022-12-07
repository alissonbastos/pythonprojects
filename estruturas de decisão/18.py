# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
print('Insira uma data no formato dd/mm/aaaa')
dia = int(input('Insira o dia no formato dd: '))
mes = int(input('Insira o mês no formato mm: '))
ano = int(input('Insira o ano no formato aaaa: '))
testadata = False

if 1 <= mes <= 12:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if 1 <= dia <= 31:
            testadata = True
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if 1 <= ano <= 9999:
        testadata = True
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        testadata = True
        if dia <= 29:
            testadata = True
    else:
        if dia <= 28:
            testadata = True
if testadata:
    print(f'Data informada: {dia}/{mes}/{ano}\n'
          f'Data válida')
else:
    print('Data informada, Iválida')



