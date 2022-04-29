#Faça um Programa que leia três números e mostre-os em ordem decrescente.
contador = maior = medio = menor = numero = 0

while contador < 3:
    numero = int(input('Digite um numero inteiro: '))
    contador += 1
    if contador == 1:
        maior = numero
    else:
        if numero >= maior:
            menor = medio
            medio = maior
            maior = numero
        elif numero <= medio:
            menor = numero
        else:
            menor = medio
            medio = numero

print(f'Os numeros digitados em ordem decrescente são: {maior}, {medio} e {menor}')


