print('Bem vindo ao controle de funcionários do Alisson Paulo Pereira Bastos')
print('RU : 4254643')
print('*' * 69)


# Variáveis globais
cadastros = []
codigo_funcionario = 750


#   FUNÇÃO PARA REALIZAR O CADASTRO DO FUNCIONÁRIO
def cadastro_funcionario(codigo):
    print('-------------------MENU CADASTRO DE FUNCIONÁRIOS-------------------')
    print(f'Código do funcionário: {codigo}')
    nome = input('Entre com o NOME: ')
    setor = input('Entre com o SETOR: ')
    salario = input('Entre com o SALÁRIO (R$):  ')
    dicionario_cadastros = {'Código':   codigo,
                            'Nome':     nome,
                            'Setor':    setor,
                            'Salário':  salario}
    cadastros.append(dicionario_cadastros.copy())
    #OS DADOS CAPTADOS SÃO COPIADOS PARA A LISTA PRINCIPAL
    print('Cadastro realizado com sucesso!')

#   Função para consultar funcionário ativo no sistema
def consultar_funcionario():
    print('-------------------MENU CONSULTA DE FUNCIONÁRIOS--------------------')
    while True:
        opcao_consultar = int(input('Escolha a opção desejada:\n'
                                    '1-Consultar todos os funcionários\n'
                                    '2-Consultar funcionários pelo CÓDIGO\n'
                                    '3-Consultar funcionários pelo SETOR\n'
                                    '4-Retornar\n'
                                    '>>>'))
        # AQUI É FEITA A COMPARAÇÃO DA OPÇÃO ESCOLHIDA, COM BASE NA OPÇÃO, O PROGRAMA VERIFICA AS OPÇÕES
        # E RETORNA O RESULTADO, IMPRIMINDO OS RESPECTIVOS DADOS SOLICITADO PELO USUÁRIO
        if opcao_consultar == 1:
            print('Funcionários cadastrados no Sistema: ')
            print('-' * 69)
            for i in cadastros:
                print('_' * 69)
                for key, value in i.items():
                    print(f'{key}: {value}')
            print('-' * 69)

        elif opcao_consultar == 2:
            codigo_consulta = int(input('Digite o CÓDIGO do funcionário para consulta:\n'
                                        '>>> '))
            for i in cadastros:
                if i['Código'] == codigo_consulta:
                    for key, value in i.items():
                        print(f'{key}: {value}')
            print('-' * 69)

        elif opcao_consultar == 3:
            codigo_consulta = input('Digite o SETOR do funcionário para consulta:\n'
                                    '>>> ')
            for i in cadastros:
                if i['Setor'] == codigo_consulta:
                    for key, value in i.items():
                        print(f'{key}: {value}')
            print('-' * 69)

        elif opcao_consultar == 4:
            return
        else:
            print('Opção selecionada inválida')
            continue

# FUNÇÃO PARA REMOVER FUNCIONÁRIOS DO CADASTRO
def remover_funcionario():
    opcao_remover = int(input('Digite o código do funcionário que deseja remover: '))
    for item in cadastros:
        if item['Código'] == opcao_remover:
            cadastros.remove(item)
            print('Funcionário REMOVIDO do sistema')


# PROGRAMA PRINCIPAL, MENU PRINCIPAL DO PROGRAMA
while True:
    opcao = int(input('Escolha a opção desejada:\n'
                      '1-Cadastrar Funcionário\n'
                      '2-Consultar Funcionário\n'
                      '3-Remover Funcionário\n'
                      '4-Sair\n'
                      '>>>'))
# VALOR RECEBIDO DO USUÁRIO É VERIFICADO ATRAVÉS DAS CONDIÇÕES
# EM CADA CONDIÇÃO CONTÉM A CHAMADA DE UMA FUNÇÃO ESPECÍFICA
    if opcao == 1:
        codigo_funcionario += 1
        print(cadastro_funcionario(codigo_funcionario))
    elif opcao == 2:
        consultar_funcionario()
    elif opcao == 3:
        remover_funcionario()
    elif opcao == 4:
        break
    else:
        print('Opção Inválida')
        continue
print('Encerrando Programa...')
