# A Confederação Nacional de Natação precisa de um program que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos - mirim; até 14 anos - infantil; até 19 anos - junior; até 20 anos -senior; acima -master

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = ano_atual - ano_nascimento

if idade < 9:
    categoria = "Mirim"
elif idade <= 14:
    categoria = "Infatil"
elif idade <= 19:
    categoria = "Junior"
elif idade <= 20:
    categoria = "Senior"
else:
    categoria = "Master"
print(f'Categoria {categoria} (Idade: {idade} anos)')