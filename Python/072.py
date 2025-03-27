'''72 - Crie um programa que tenha uma tupla totalmente preenchida por uma contagem por extenso de 0 até vinte. 
Seu programa deve ler um número pelo teclado entre 0 e vinte e mostrá-lo por extenso.'''

tupla = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

valor = int(input("Escolha um número inteiro de 0 a 20: "))
print(f'O número que você escolheu, escrito por extenso é {tupla[valor]}')