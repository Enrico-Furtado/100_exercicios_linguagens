'''15 - Escreva um programa que pergunte a quantidade de km rodados por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar sabendo que o carro custa R$60.00 por dia e R$0.15 por km percorrido.'''

dia = int(input('Por quantos dias o carro foi alugado? '))
kilo = float(input('Quanto km o carro percorre? '))
preco = (60 * dia) + (kilo * 0.15)
print(f'O preço total a pagar pelo carro alugado é de: R$ {preco:.2f}.')