'''35 - Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.'''

print('Digite abaixo 3 retas e vamos saber se podemos construir um triângulo a partir delas!')
r1 = int(input('Primeira Reta:'))
r2 = int(input('Segunda Reta:'))
r3 = int(input('Terceira Reta:'))

if (r1+r2)>r3 and (r2+r3)>r1 and (r1+r3)>r2:
    print('Podemos construir um triângulo com essas retas.')
else:
    print('Não podemos construir um triângulo com essas retas!')