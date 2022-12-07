'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
tinta a serem compradas e o preço total.'''

print('Inicio do programa')
metros = float(input('Digite o tamanho da área em metros quadrados a ser pintada:\n>>>'))
litros = metros / 3
precoL = 80
capacidadeL = 18

latas = litros / capacidadeL
total =latas * precoL


print(f'Quantidade de lata a serem compradas é: {latas} \n Total = R${total}')