# EXERCÍCIO 8 - Escreva um programa que leia um valor em metros e converta ele em centímetros e milímetros.

metr = float(input('Digite um valor em metros: '))
cm = metr * 100
mm = metr * 1000

print(f'{metr}m equivale a {cm}cm ou também a {mm}mm.')