#Faça um Programa que peça dois números e imprima o maior dele

numero1 = int(input("Digite um numero: "))
numero2 = int(input('Digite outro numero: '))
if numero1 > numero2:
    print(f'O maior numero é {numero1}')
elif numero1 < numero2:
    print(f'O maior numero é {numero2}')
else:
    print('Ambos os numeros são iguais')




