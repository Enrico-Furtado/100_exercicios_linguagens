'''50 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar, desconsidere-o.'''

print("Digite 6 números inteiros e veremos qual a soma dos números pares dentre eles.")
soma = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i} número.'))
    if num % 2 == 0:
        soma += num
print(f"A soma dos números pares deu {soma}. Você informou {i} números.")