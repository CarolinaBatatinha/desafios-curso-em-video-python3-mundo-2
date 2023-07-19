# Crie um programa que faça o computador jogar "pedra, papel e tesoura" com você.
from random import randint
from time import sleep
print('''
Escolha seu movimento!
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA ''')
player1 = int(input('Sua opção: '))
pedra = 1
papel = 2
tesoura = 3
computador = randint(1,3)

print(f'Movimento do computador: {computador}')
print(f'\nVocê escolheu {player1} e o computador escolheu {computador}.')

if player1 == pedra and computador == tesoura:
    print(f'Você VENCEU!')
elif computador == pedra and player1 == tesoura:
    print('O computador VENCEU!')
elif computador == tesoura and player1 == papel:
    print(f'O computador VENCEU!')
elif player1 == tesoura and computador == papel:
    print('Você VENCEU!')
elif player1 == papel and computador == pedra:
    print('Você VENCEU!')
elif computador == papel and player1 == pedra:
    print('O computador VENCEU!')
else:
    print('Empate! Jogue novamente!')
