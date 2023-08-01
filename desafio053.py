# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços e acentos.
# ex: apos a sopa

frase = str(input('\nDigite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1 ):
    inverso += junto[letra]

if inverso == junto:
    print('Temos um palíndromo!')
    print(f'O inverso de {junto} é {inverso}.')
else:
    print('A frase digitada não é um palíndromo.')
    print(f'O inverso de {junto} não é {inverso}.')

