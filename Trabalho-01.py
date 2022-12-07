#Identificação do Autor:

print('Bem vindo a Loja do Alisson Paulo Pereira Bastos')
print('RU: 4254643')

'''Inicio do programa
   As variavéis valor e quantidade são definidas e seus valores são atribuídos pelo usuário.
'''
valor = float(input('Entre com o valor unitário do produto: \n>>>'))
quantidade = int(input('Entre com a quantidade do produto: \n>>>'))

'''A variavél (subtotal) recebe o valor do produto, e é multiplicado pela variavél quantidade 
   obtendo o subtotal do carrinho.
'''
subtotal = float(valor * quantidade)

#Mensagem mostrada ao usuário após somados os valores, sem o frete.
print(f'O valor total sem frete foi: R$ {subtotal}')

#Inicio da comparação dos valores referentes a quantidade desejada pelo usuário.
#Caso uma das opções forem válidas, é mostrado o resultado com o valor do frete.
if 0 <= quantidade < 11:
    total = 30.00 + subtotal
    print(f'O valor total com o frete foi: R$ {total:.2f} '
          f'(Frete R$ 30,00)')

elif 11 <= quantidade < 101:
    total = 60.00 + subtotal
    print(f'O valor total com o frete foi: R$ {total:.2f} '
          f'(Frete R$ 60,00)')

elif 101 <= quantidade <1001:
    total = 120.00 + subtotal
    print(f'O valor total com o frete foi: R$ {total:.2f} '
          f'(Frete R$ 120,00)')

elif quantidade >= 1001:
    total = 240 + subtotal
    print(f'O valor total com o frete foi: R$ {total:.2f} '
          f'(Frete R$ 240,00)')

else:
    print('Dados inexistentes!')

'''Caso usuário não entrou com os valores correspondentes a quantidade que define o valor do frete, 
o programa encerra.
'''
print('\nFIM DO PROGRAMA')
