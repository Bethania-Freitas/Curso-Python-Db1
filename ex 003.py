#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = str(input('Digite seu sexo[F/M]:  ')).strip().upper()[:1]
if sexo in 'Ff':
    print('Feminino')
else:
    print('Masculino')