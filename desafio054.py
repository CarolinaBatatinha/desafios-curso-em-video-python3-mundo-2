# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Considere a maioridade com 21 anos.

import datetime

maioridade = 0
menoridade = 0
data_atual = datetime.datetime.now()
ano_atual = data_atual.year

for i in range(1,8): 
    ano_nascimento = int(input(f'Informe o ano de nascimento da {i}ª pessoa: '))
    
    if ano_atual - ano_nascimento >= 21:
        maioridade += 1
    else:
        menoridade += 1
print(f'\n{maioridade} pessoas já atingiram a maioridade.')
print(f'{menoridade} pessoas não atingiram a maioridade.')
