'''42 - Refaça o exercício 35 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo está sendo formado. 
EQUILÁTERO(todos os lados iguais). 
ISÓSCELES(dois lados iguais). 
ESCALENO(todos os lados diferentes).'''

print('Digite abaixo 3 retas e vamos saber se podemos construir um triângulo a partir delas!')
r1 = int(input('Primeira Reta:'))
r2 = int(input('Segunda Reta:'))
r3 = int(input('Terceira Reta:'))

if (r1+r2)>r3 and (r2+r3)>r1 and (r1+r3)>r2:
    print('Podemos construir um triângulo com essas retas.')
    if r1 == r2 == r3:
        print("O triângulo é EQUILÁTERO!")
    elif r1 == r2 or r1 ==r3 or r3 == r2:
        print("O triângulo é ISÓSCELES!")
    elif r1 != r2 != r3 != r1:
        print("O triângulo é ESCALENO!")
else:
    print('Não podemos construir um triângulo com essas retas!')