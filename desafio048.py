# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 a 500.

soma = 0
cont = 0

for i in range(1, 500):
    if i % 2 == 1 and i % 3 == 0:
        soma += i
        cont += 1
print(f'A soma dos {cont} números é igual a {soma}.')