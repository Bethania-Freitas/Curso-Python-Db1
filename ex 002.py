#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

numero = int(input('Digite um numero: '))
if numero > 0:
    print(f'O numero {numero} é positivo')
elif numero == 0:
    print(f'O numero {numero} é neutro')
else:
    print(f'O numero {numero} é negativo')