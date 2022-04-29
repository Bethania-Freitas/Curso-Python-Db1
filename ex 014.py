#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

print('Vamos analisar um triangulo')
print('_'*20)
l1 = float(input('Digite o comprimeiro de 1 dos lado: '))
l2 = float(input('Digite o comprimento do segundo lado: '))
l3 = float(input('Digite o comprimento do terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Isto é um triangulo', end=' ')
    if l1 == l2 == l3:
        print('EQUILATERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print ('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Isto não forma um trinagulo')