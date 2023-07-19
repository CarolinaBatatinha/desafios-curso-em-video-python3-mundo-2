# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: média abaixo de 5 - reprovado; média entre 5 e 6.9 - recuperação; ou média 7 ou superior: aprovado.

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 +  nota2) / 2

if media < 5:
    print(f'Reprovado.\nMédia: {media:.1f}')
elif 5 < media < 7:
    print(f'Recuperação.\nMédia: {media:.1f}')
else:
    print(f'Aprovado.\nMédia: {media:.1f}')