# Refaça o desafio035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: equilátero (todos os lados iguais), isósceles (dois lados iguais), ou escaleno (todos os lados diferentes).

reta1 = int(input('Informe o comprimento da primeira reta: '))
reta2 = int(input('Informe o comprimento da segunda reta: '))
reta3 = int(input('Informe o comprimento da terceira reta: '))



if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta3 + reta2) > reta1:
    print('É possível formar um triângulo com as medidas informadas.')
    if reta1 == reta2 == reta3:
        print('Triângulo equilátero')
    elif reta1 != reta2 != reta3:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')
        
else:
    print('Não é possível formar um triângulo com as medidas informadas.') #ARRUMAR!!