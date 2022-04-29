#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c

a = float(input('Digite valor de A: '))
b = float(input('Digite valor de B: '))
c = float(input('Digite valor de C: '))
delta = b**2 - (4*a*c)
raizdelta = delta**0.5

x1 = (-b + raizdelta) / (2*a)
x2 = (-b - raizdelta) / (2*a)

print(f'x1 = {x1}')
print(f'x2 = {x2}')