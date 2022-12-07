# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino
# ou N- Noturno.Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input('Digite o turno que você estuda:\n'
              'M - Matutino\n'
              'V - Vespertino\n'
              'N - Noturno\n'
              '>>>')

if turno.upper() == 'M':
    print('Bom dia!')
elif turno.upper() == 'V':
    print('Boa Tarde!')
elif turno.upper() == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido')