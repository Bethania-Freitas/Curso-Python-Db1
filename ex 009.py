#Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-Matutino ou V- Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

turno = str(input('Qual o turno que você estuda? [M - matutino/ V - Vespertino / N - Noturno]')).strip().upper()[:1]
if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print('Boa tarde')
elif turno == 'N':
    print('Boa noite')
else:
    print('Valor Inválido')
