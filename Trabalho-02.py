print('Bem vindo a loja do Alisson Paulo Pereira Bastos')
print('RU 4254643')
print('--------------------------------------------Cardápio----------------------------------------------\n'
      '|  Código   | Descrição            | Tamanho p (500ml) | Tamanho M (1000ml) | Tamanho G (1000ml) |\n'
      '|    TR     | Sabores tradicionais |      R$ 6,00      |      R$ 10,00      |       R$ 18,00     |\n'
      '|    ES     | Sabores Especiais    |      R$ 7,00      |      R$ 12,00      |       R$ 21,00     |\n'
      '|    PR     | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |       R$ 24,00     |\n'
      '--------------------------------------------------------------------------------------------------')
total = 0
while True: #Laço de repetição testando as condições inseridas pelo usuário
    tamanho = str(input('Entre com o TAMANHO do pote de sorvete desejado (P/M/G): '))
    tamanho = tamanho.upper()   # Função que resolve a entrada de letras maiúsculas e menúsculas

    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G' :
        print('Opção Inválida!!! Tamanho digitado inválido!!!')
        continue

    codigo = str(input('Entre com o CÓDIGO do sabor de sorvete desejado (TR/ES/PR): '))
    codigo = codigo.upper()
    if codigo != 'TR' and codigo != 'tr' and codigo != 'ES' and codigo != 'es' and codigo != 'PR' and codigo != 'pr':
        print('Opção Inválida!!! Codigo digitado inválido!!!')
        continue
    #testando condições de valores de entrada
    if codigo == 'TR' and tamanho == 'P':
        total += 6.00
        print(f'Você escolheu Sabores Tradicionais, Tamanho Pequeno, Total de {total}')
    elif codigo == 'TR' and tamanho == 'M':
        total += 10.00
        print(f'Você escolheu Sabores TRadicionais, Tamanho Médio, Total de {total}')
    elif codigo == 'TR' and tamanho == 'G':
        total += 18.00
        print(f'Você escolheu Sabores Tradicionais, Tamanho Grande, Total de {total}')
    elif codigo == 'ES' and tamanho == 'P':
        total += 7.00
        print(f'Você escolheu Sabores Especiais, Tamanho Pequeno, Total de {total}')
    elif codigo == 'ES' and tamanho == 'M':
        total += 12.00
        print(f'Você escolheu Sabores Especiais, Tamanho Médio, Total de {total}')
    elif codigo == 'ES' and tamanho == 'G':
        total += 21.00
        print(f'Você escolheu Sabores Especiais, Tamanho Grande, Total de {total}')
    elif codigo == 'PR' and tamanho == 'P':
        total += 8.00
        print(f'Você escolheu Sabores Premium, Tamanho Pequeno, Total de {total}')
    elif codigo == 'PR' and tamanho == 'M':
        total += 14.00
        print(f'Você escolheu Sabores Premium, Tamanho Médio, Total de {total}')
    elif codigo == 'PR' and tamanho == 'G':
        total += 24.00
        print(f'Você escolheu Sabores Premium, Tamanho Grande, Total de {total}')

    '''Teste de continuidade de pedidos, se a resposta for sim, então o laço volta ao inicio do programa
        senão ocorre o break e fecha a conta mostrando o total'''

    resposta = input('Deseja adicionar mais algum pedido? (S/N): ')
    resposta = resposta.upper()
    if resposta == 'N':
        break
    else:
        continue

print(f'Pedido realizado com sucesso, o valor total foi de: R$ {total:.2f}')
