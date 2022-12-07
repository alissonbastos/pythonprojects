# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário
# o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas


quant_horas = float(input('Quanto você ganha por hora?\n>>>'))
horas_trabalhadas = float(input('Horas trabalhadas no mês\n>>>'))
salario_bruto = quant_horas * horas_trabalhadas
imposto = 0

if salario_bruto < 900:
    print('Isento de Imposto de renda\n'
          'Alíquota não se aplica')
elif salario_bruto > 900 and salario_bruto <= 1500:
    IR = (salario_bruto * 10 / 100)
    imposto = IR
    print('-Aliquota 10%')
elif salario_bruto > 1500 and salario_bruto <= 2500:
    IR = (salario_bruto * 15 / 100)
    imposto = IR
    print('-Aliquota 15%')
elif salario_bruto > 2501:
    IR = (salario_bruto * 20 / 100)
    print('-Aliquota 20%')
    imposto = IR

INSS = (salario_bruto * 8 / 100)
sindicato = (salario_bruto * 5 / 100)
salario_liquido = int(salario_bruto - imposto - INSS - sindicato)
print(f'- IR: R$ {imposto}')
print(f'+ Salário Bruto : R$ {salario_bruto}')
print(f'- INSS (8%) : R$ {INSS}')
print(f'- Sindicato ( 5%) : R$ {sindicato}')
print(f'= Salário Liquido : R$ {salario_liquido}')

