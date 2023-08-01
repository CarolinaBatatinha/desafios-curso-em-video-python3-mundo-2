# Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre: 
# a média de idade do grupo;
# qual o nome do homem mais velho;
# quantas mulheres tem menos de 20 anos.

soma_idade = 0
media_idade = 0
idade_homem_mais_velho = 0
nome_mais_velho = ''
total_feminino_20_menos = 0

for i in range(1, 5): 
    print(f'\n:.: {i}ª pessoa :.:')
    nome = str(input('\nNome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip()
    soma_idade += idade
    
    if i == 1 and sexo in 'Mm':
        idade_homem_mais_velho = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade > 20:
        total_feminino_20_menos += 1
    media_idade = soma_idade / 4
    
print(f'A média das idades é igual a {media_idade}.')
print(f'O nome do homem mais velho é {nome_mais_velho} e ele tem {idade_homem_mais_velho} anos.')
print(f'O número de mulheres com menos de 20 anos é igual a {total_feminino_20_menos}')
    