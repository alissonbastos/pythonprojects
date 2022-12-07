# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo
# de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2

#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E

mensagem = 0
if 9.0 <= media < 10.0:
    mensagem = 'Conceito A\nAprovado'
elif 7.5 <= media < 9.0:
    mensagem = 'Conceito B\nAprovado'
elif 6.0 <= media < 7.5:
    mensagem = 'Conceito C\nAprovado'
elif 4.0 <= media < 6.0:
    mensagem = 'Conceito D\nReprovado'
elif 0 <= media < 4.0:
    mensagem = 'Conceito E\nReprovado'

# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO”
# se o conceito
# for A, B ou C ou “REPROVADO” se o conceito for D ou E.

print(f'Nota 1ª: {nota1}\nNota 2ª: {nota2}\nMédia: {media} - {mensagem}')