'''39 - Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade: 
- Se ele ainda vai se alistar ao serviço militar. Se é a hora de se alistar. 
Se já passou do tempo do alistamento. Seu programa também deve mostrar o tempo que falta ou que passou do prazo.-'''
from datetime import date

print("Diga o seu ano de nascimento e veremos se está na hora do seu alistamento militar!")
nasc = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nasc
if idade > 18:
    delta_p = idade - 18
    print(f"Já passou {delta_p} anos do prazo do seu alistamento.")
elif idade < 18:
    delta_pr = 18 - idade
    print(f'Faltam {delta_pr} anos para o seu alistamento.')
else:
    print("É a hora perfeita para se alistar!")