print('Bem vindo ao programa de Serviços do Alisson Paulo Pereira Bastos')
print('RU 4254643')
print('*' * 81)


'''Inicio da função limpeza'''


def metragem_limpeza():
    print('*' * 35 + ' Menu 1 de 3 ' + '*' * 33)
    global y
    y = 0
    while True:
        try:
            metragem = int(input(f'Entre com o valor do M² do local:\n'))
            if (metragem >= 30) and (metragem <= 300):
                print('Será necessário um(a) funcionário(a) para a limpeza\n')
                y += 60 + 0.3 * metragem
                return y
            elif (metragem > 300) and (metragem <= 700):
                print('Serão necessários dois(uas) funcionários(as) para a limpeza\n')
                y += 120 + 0.5 * metragem
                return y
            else:
                print('Trabalhamos apenas com metragem acima de 30 M² e máximo de 700 M²')
                continue
        except ValueError:
            print(f'O Valor digitado está inválido, Tente Novamente!!!\n>>>')


'''inicio da função tipo de limpeza'''


def tipo_limpeza():
    print('*' * 35 + ' Menu 1 de 3 ' + '*' * 33)
    global x
    x = 0
    while True:
        limpeza = str(input('Qual o tipo da limpeza desejada?\n'
                            'B - Básica - Recomendado para sujeiras semanais ou quinzenais\n'
                            'C - Completa (30% a mais) - Recomendado para sujeiras antigas e/ou não rotineiras\n'
                            '---------------------------------------------------------------------------------\n'
                            '>>>'))
        limpeza = limpeza.upper()
        if limpeza == 'B':
            print('Limpeza escolhida: BÁSICA\n')
            x += 1.00
            return x
        elif limpeza == 'C':
            print('Limpeza escolhida: COMPLETA\n')
            x += 1.30
            return x
        else:
            print('Tipo de limpeza inválida, Por favor tente novamente\n'
                  '>>>')
            continue


'''Inicio da função adicional de limpeza'''


def adicional_limpeza():
    print('*' * 35 + ' Menu 1 de 3 ' + '*' * 33)
    global z
    z = 0
    while True:
        try:
            adicional = int(input(f'Deseja algum adicional? \n'
                                  f'0 - Não desejo mais nada  (Encerrar)\n'
                                  f'1 - Passar dez peças de roupas - R$ 10,00\n'
                                  f'2 - Limpeza de 1 Forno/Microondas - R$ 12,00\n'
                                  f'3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00\n'
                                  f'>>>'))
            if adicional == 0:
                return z
            elif adicional == 1:
                z += 10.00
                continue
            elif adicional == 2:
                z += 12.00
                continue
            elif adicional == 3:
                z += 20.00
                continue
            else:
                print('Opção Inválida!')
                continue
        except ValueError:
            print('Opção Inválida,Por favor digite um valor dentre as opções abaixo!')
            continue


'''variáveis recebem os resultados através das funções'''
y = metragem_limpeza()
x = tipo_limpeza()
z = adicional_limpeza()

'''calculo do resultado final'''
total = (y * x) + z

print('*' * 80)
print(f'TOTAL: R$ {total:.2f} \n')
print(f'(Metragem: {y:.2f} * Tipo: {x:.2f}) + Adicional(ais): R$ {z:.2f}')
