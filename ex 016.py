#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

from datetime import date
ano = int(input('digite o ano que deseja saber se é bissexto, 0 para o ano atual:' ))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Sim, o ano de \033[32m{}\033[m é um ano bissexto'.format(ano))
else:
    print('Não, o ano de \033[33m{}\033[m não é um ano bissexto'.format(ano))