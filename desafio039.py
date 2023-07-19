# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alista ao serviço militar, se é a hora de se alistar, ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input('Informe o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print('É hora de você se alistar!')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar.')
else:
    print(f'Você já passou {idade - 18} anos do prazo de alistamento.')