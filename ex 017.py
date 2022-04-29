#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida

dias = int(input('Informe uma data (dd/mm/aaaa) - Dias: '))
mes = int(input('Informe uma data (dd/mm/aaaa) - Mes: '))
ano = int(input('Informe uma data (dd/mm/aaaa) - Ano: '))
meses_31 = [1, 3, 5, 7, 8, 10, 12]
meses_30 = [4, 6, 9, 11]

def ano_bissexto():
    if (ano%4 == 0) and (ano%400 == 0) and (not ano%100):
        return True
    else:
        return False
ano_bisx = ano_bissexto()

def dias_bissexto():
    if (ano_bisx == True) and (mes == 2) and (dias >= 1 and dias <= 29):
        print('Data válida\n')
    if ano_bisx == True:
        print('Esse ano é bissexto')
    elif(ano_bisx == False) and (mes == 2) and (dias >= 1 and dias <= 28):
        print('Data válida\n')
    if ano_bisx == False:
        print('Esse ano não é bissexto')
    elif(ano_bisx == True) and (mes == 2) and (dias >= 1 and dias > 28):
        print('Data invalida')
    elif(ano_bisx == False) and (mes == 2) and (dias >= 1 and dias > 28):
        print('Data invalida')
dias_biss = dias_bissexto()

def mes_comuns():
    if (mes in meses_31) and ( dias >= 1 and dias <= 31):
        print('Data válida \n')
    if ano_bisx == True:
        print('Esse ano é bissexto')
    elif (mes in meses_30) and (dias >= 1 and dias <= 30 ):
        print('Data válida \n')
    if ano_bisx == True:
        print('Esse ano é bissexto')
    elif (mes in meses_30) and (dias >= 1 and dias > 30 ):
        print('Data invalida')
    elif (mes in meses_31) and (dias >= 1 and dias > 31 ):
        print('Data invalida')
mes_com = mes_comuns()

