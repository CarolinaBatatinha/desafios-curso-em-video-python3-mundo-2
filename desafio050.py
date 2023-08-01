# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.
soma = 0
cont = 0

for contador in range(1, 7):
    num = int(input(f'Digite o {contador}º número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont+= 1
    
print(f'\nA soma dos {cont} números pares é igual a {soma}.')