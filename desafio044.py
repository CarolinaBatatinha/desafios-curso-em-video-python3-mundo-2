# Elabora um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:

# - à vista dinheiro/ cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor_produto = float(input('Digite o valor do produto: '))
opcao = int(input('''
Informe a forma de pagamento:
[1] - à vista (dinheiro ou cheque)
[2] - à vista (cartão)
[3] - até 2 vezes no cartão
[4] - 3 ou mais vezes no cartão
'''))

if opcao == 1:
    valor_final = valor_produto - (valor_produto * .1)
    print('Pagamento à vista (dinheiro ou cheque)')
elif opcao == 2:
    valor_final = valor_produto - (valor_produto * .05)
    print('Pagamento à vista (cartão)')
elif opcao == 3:
    valor_final = valor_produto
    print('Pagamento em até 2x no cartão')
else:
    valor_final = valor_produto * 1.2
    print('Pagamento em até 3x no cartão')
    
print(f'Valor normal do produto: R$ {valor_produto:.2f}')
print(f'Valor a ser pago: R$ {valor_final:.2f}')