#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
# 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.#
# Desconto do IR:
# Salário Bruto até 900 (inclusive) – isento
# Salário Bruto até 1500 (inclusive) – desconto de 5%
# Salário Bruto até 2500 (inclusive) – desconto de 10%
# Salário Bruto acima de 2500 – desconto de 20% Imprima na tela as informações

horasTrabalhadas = float(input('Quantas horas foram trabalhadas? '))
valorHora = float(input('Qual valor da hora do funcionario: '))
salarioBruto = horasTrabalhadas * valorHora
sindicato = salarioBruto/100 * 3
fgts = salarioBruto/100 * 11
salarioLiquido = 0
ir = 0

print(' ')
print('-----FOLHA DE PAGAMENTO-----')
print(f'Salario Bruto: R$ {salarioBruto:.2f}')
print(f'Sindicato: R$ {sindicato:.2f}')
print(f'Valor FGTS: R$ {fgts:.2f}')

if salarioBruto <= 900:
    ir = 0
elif salarioBruto <= 1500:
    ir = salarioBruto/100 * 5
elif salarioBruto <= 2500:
    ir = salarioBruto/100 * 10
else:
    ir = salarioBruto/100 * 20

salarioLiquido = salarioBruto - sindicato - ir
print(f'IR: {ir:.2f}')
print(f'Salario Liquido: R$ {salarioLiquido:.2f}')

