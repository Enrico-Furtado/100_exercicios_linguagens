'''40 - Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem final de acordo com a média atingida. 
Média abaixo de 5.0: REPROVADO. Média entre 5.0 e 6.9: RECUPERAÇÃO. Média 7.0 ou superior: APROVADO.'''

nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
media = (nota_1 + nota_2)/2
print(f"Sua média foi de {media} pontos.")
if media < 5.0:
    print("Você está REPROVADO!")
elif 5.0 <= media <= 6.9:
    print("Você está de RECUPERAÇÃO!")
else:
    print("Você está APROVADO!")