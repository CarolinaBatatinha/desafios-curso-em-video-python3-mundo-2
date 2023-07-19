# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo

# Abaixo de 18.5:             abaixo do peso
# Entre 18.5 e 25:            peso ideal
# Entre 25 e 30:              sobrepeso
# Entre 30 e 40:              obesidade
# Acima de 40:                obesidade mórbida

from math import pow

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print(f'IMC = {imc:.1f} - Abaixo do peso. ')
elif 18.5 <= imc < 25:
    print(f'IMC = {imc:.1f} - Peso ideal. ')
elif 25 <= imc < 30:
    print(f'IMC = {imc:.1f} - Sobrepeso. ')
elif 30 <= imc < 40:
    print(f'IMC = {imc:.1f} - Obesidade. ')
else:
    print(f'IMC = {imc:.1f} - Obesidade mórbida. ')