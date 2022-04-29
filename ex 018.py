#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo

numero = int(input('Digite um numero até 999: '))
unidade = numero % 10
dezena = ((numero - unidade) / 10) % 10
centena = int(numero / 100)
print(f'Unidade: {unidade:.0f}')
print(f'Dezena: {dezena:.0f}')
print(f'Centena: {centena:.0f}')