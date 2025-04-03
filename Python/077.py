'''77 - Crie um programa que tenha uma tupla com várias palavras, não usar acentos. Depois, você deve mostrar para cada palavra, 
quais são suas vogais.'''

tupla = ("rocket","derivada","integral","linear","laplace")
for i in tupla:
    print(f"Na palavra {i.upper()} temos as vogais: ", end=" ")
    for p in i:
        if p.lower() in "aeiou":
            print(f"{p}", end=" ")
    print("\n")
