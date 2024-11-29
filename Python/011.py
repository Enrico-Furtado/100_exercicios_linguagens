'''EXERCÍCIO 11 - Faça um programa que leia a altura e a largura de uma parede em metros, calcule a área dessa parede e o quanto de tinta dever ser utilizada pra pintar.
Considerando que 1 litro pinta 2 metros quadrados.'''

alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
tinta = area / 2
print(f'A parede possui {area} m2 e assim, {tinta} litros de tinta serão gastos para pintá-la.')