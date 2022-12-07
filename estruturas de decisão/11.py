'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input('Digite o valor do salário: '))

if salario < 280:
    percentual = (salario * 20) / 100
    total = salario + percentual
    print(f'Salário sem reajuste: R$ {salario}\nPercentual aplicado 20%\nValor do aumento aplicado: {percentual}\n'
          f'Novo salário: {total}')
elif 280 < salario <= 700:
    percentual = (salario * 15) / 100
    total = salario + percentual
    print(f'Salário sem reajuste: R$ {salario}\nPercentual aplicado 15%\nValor do aumento aplicado: {percentual}\n'
          f'Novo salário: {total}')
elif 700 < salario <= 1500:
    percentual = (salario * 10) / 100
    total = salario + percentual
    print(f'Salário sem reajuste: R$ {salario}\nPercentual aplicado 10%\nValor do aumento aplicado:  {percentual}\n'
          f'Novo salário: {total}')
elif salario > 1501:
    percentual = (salario * 5) / 100
    total = salario + percentual
    print(f'Salário sem reajuste: R$ {salario}\nPercentual aplicado 5%\nValor do aumento aplicado:  {percentual}\n'
          f'Novo salário: {total}')
