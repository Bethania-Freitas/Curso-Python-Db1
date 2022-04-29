#Faça um Programa que verifique se uma letra digitada é vogal ou consoante
letra = str(input('Digite uma letra pra saber se é vogal ou consoante: ')).strip().upper()
if letra in 'AEIOU':
    print(f'A letra "{letra}" é uma vogal')
else:
    print(f'A letra "{letra}" é uma consoante')