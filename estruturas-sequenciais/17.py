'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
 sempre arredonde os valores para cima, isto é, considere latas cheias.'''

print('Inicio do programa')
metros = float(input('Digite o tamanho da área em metros quadrados a ser pintada:\n>>>'))

#calculo em latas de 18L
litros = metros / 6
precoL = 80
capacidadeL = 18
latas = (litros / capacidadeL)
total = latas * precoL

#calculo em galões de 3,6L
Preco_G = 25
capacidade_G = 3.6
galoes = litros / capacidade_G
total2 = galoes * Preco_G


print(f'Quantidade de lata a serem compradas: {latas:.2f} \n Total = R${total:.2f}')
print(f'Quantidade em galões a ser compradas: {galoes:.2f}\n Total = R${total2:.2f}')

