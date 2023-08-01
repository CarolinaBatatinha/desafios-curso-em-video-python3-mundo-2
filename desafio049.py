# Mostre a tabuada de um número que o usuário escolher utlizando um laço "for".

num = int(input('Escolha um número: '))
print(f'==== TABUADA DE {num} ====')

for i in range(1, 11):
    res = num * i
    print(f'{num} x {i:2} = {res}')# esse :2 dá o espaçamento pra tabular a tabuada
