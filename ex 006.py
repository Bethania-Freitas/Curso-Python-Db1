#Faça um Programa que leia três números e mostre o maior e o menor deles
n = maior = 0
menor = 1
while n < 3:
    n1 = int(input('Digite um numero: '))
    n += 1
    if n1 > maior:
        maior = n1
    else:
        menor = n1

print(f'O maior numero digitado é o {maior} e o menor é o {menor}')
