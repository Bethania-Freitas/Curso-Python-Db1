#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: Média de Aproveitamento
# Conceito Entre 9.0 e 10.0 A
# Entre 7.5 e 9.0 B
# Entre 6.0 e 7.5 C
# Entre 4.0 e 6.0 D
# Entre 4.0 e zero E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
# “APROVADO” se o conceito for A, B ou C ou
# “REPROVADO” se o conceito for D ou E.

print('-------BOLETIM -------')
nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 4:
    conceito = 'E'
    status = 'Reprovado'
elif media <= 6:
    conceito = 'D'
    status = 'Reprovado'
elif media <= 7.5:
    conceito = 'C'
    status = 'Aprovado'
elif media <= 9:
    conceito = 'B'
    status = 'Aprovado'
else:
    conceito = 'A'
    status = 'Aprovado'

print(' ')
print(f'Media: {media}')
print(f'Conceito: {conceito}')
print(f'Status: {status}')


