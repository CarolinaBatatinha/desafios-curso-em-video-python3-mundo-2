# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#O número primo é divível apenas por 1 e por ele mesmo (sempre sendo igual a duas divisões)
num = int(input('\nDigite um número inteiro: '))
total_divisoes = 0
for c in range(1, num+1):
    if num % c == 0: # CONDIÇÃO PRA CONTAR A QUANTIDADE DE DIVISÕES POSSÍVEIS
        print('\033[34m', end = ' ')
        total_divisoes += 1
    else:
        print('\033[31m', end = ' ')
    print(c, end =' ')
print(f'\n\033[mO número {num} foi divisível {total_divisoes} vezes.')
if total_divisoes == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é primo!')
