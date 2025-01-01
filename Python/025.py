'''Crie um programa que leia o nome de uma pessoa e diga se ele tem 'SILVA' no nome.'''

nome = str(input("Digite o nome de uma pessoa: ")).upper().strip()
print(f"O nome contém 'SILVA'? ", 'SILVA' in nome)