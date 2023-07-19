# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_imovel = float(input('Informe o valor do imóvel a ser financiado em R$: '))
salario_comprador = float(input('Informe o salário do candidato ao financiamento em R$: '))
prazo_pagamento = int(input('Informe em quantos anos o candidato pretente quitar o financiamento: '))

valor_minimo_prestacao = salario_comprador * .3

prestacao_mensal = valor_imovel / (prazo_pagamento * 12)

if prestacao_mensal > valor_minimo_prestacao:
    print('Seu financiamento não foi aprovado.')
else:
    print(f'\nSeu financiamento foi aprovado. Sua prestação mensal durante {prazo_pagamento} anos será de R$ {prestacao_mensal:.2f}.')
