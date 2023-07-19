# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 - para binário; 2 - para octal; 3 - para hexadecimal.

num = int(input('Informe um número inteiro qualquer: '))

base_conversao = int(input('Informe a base de conversão\n1 - binário\n2 - octal\n3 - hexadecimal\n'))

if base_conversao == 1:
    
    print(f'O número {num} convertido para binário é igual a {bin(num)[2:]}.')
elif base_conversao == 2:
    print(f'O número {num} convertido para octal é igual a {oct(num)[2:]}.')
elif base_conversao == 3:
    print(f'O número {num} convertido para hexadecimal  é igual a {hex(num)[2:]}.')
else:
    print('Digite um valor válido.')