'''36 - Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o VALOR DA CASA,
 o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do 
 salário ou então o empréstimo sera negado.'''

print('Vamos ver se você consegue um empréstimo bancário para comprar uma casa!')
valor = float(input('Primeiro, me diga qual o valor da casa (reais): '))
sal = float(input('Agora me diga o seu salário (reais): '))
anos = int(input('Por fim, em quantos anos você quer pagar a casa? '))
prest = valor/(anos * 12)
limite = sal * 0.3
if prest > limite:
    print('Infelizmente não podemos realizar o empréstimo.')
else:
    print('Parabéns, o empréstimo será realizado!')

print(prest)
print(limite)