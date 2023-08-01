# Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, moestre os 10 primeiros termos desta progressão.
soma = 0

primeiro_termo = int(input('Informe o primeiro termo da progressão aritmética: '))
razao = int(input('Informe a razão da progressão aritmética: '))
decimo_termo = primeiro_termo + (10 - 1) *  razao


for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(c, end =' -> ')
print('Fim')