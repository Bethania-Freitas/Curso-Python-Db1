#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R 280,00eR  700,00 : aumento de 15%
# salários entre R 700,00eR  1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

reajuste = salarioAnterior = novoSalario = 0

salarioAnterior = float(input('Qual valor do salário atual do colaborador: '))
if salarioAnterior <= 280:
    novoSalario = salarioAnterior + (salarioAnterior/100 * 20)
    reajuste += 20
elif salarioAnterior < 700:
    novoSalario = salarioAnterior + (salarioAnterior/100 * 15)
    reajuste += 15
elif salarioAnterior < 1500:
    novoSalario = salarioAnterior + (salarioAnterior/100 * 10)
    reajuste += 10
else:
    novoSalario = salarioAnterior + (salarioAnterior/100 * 5)
    reajuste += 5
print(f'O salario que era de {salarioAnterior:.2f} teve reajuste de {reajuste}% e passa a ser de {novoSalario:.2f}')