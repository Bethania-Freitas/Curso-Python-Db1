#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print('---DIA DA SEMANA ----')
semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta','Sábado']
dia = int(input('Informe o numero correpondente ao dia da semana\n[1] - Domingo\n[2] - Segunda\n[3] - Terça\n[4] - Quarta\n[5] - Quinta\n[6] - Sexta\n[7] - Sabado\nOpção: '))
if dia < 1 or dia > 7:
    print('Opção inválida')
else:
    print(f'O dia da semana selecionado foi: {semana[dia-1]}')



