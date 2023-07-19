# Escreva um programa que leia dois números inteiros e os compares, mostrando na tela uma mensagem "o primeiro valor é maior", "o segundo valor é maior" ou "não existe valor maior, os dois são iguais."
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num1 < num2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')