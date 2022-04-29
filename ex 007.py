#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

preco = 0
barato = 0

while preco < 3:
    barato1 = float(input('Digite o preço do produto: '))
    preco += 1
    if preco == 1:
        barato = barato1
    else:
        if barato1 < barato:
            barato = barato1
print(f'O produto de {barato} é o mais barato da lista')

