"""
Crie um algoritmo que lê um número e mostre o seu dobro, seu triplo e sua raiz quadrada
"""
número = int(input("Digite um valor numérico: "))

dobro = número * 2

triplo = número * 3

square_root = número ** (1/2) # Se quiser pode usar a função pow(), ela também retorna a raiz quadrada de um número

print(f"O dobro de {número} é {dobro}")
print(f"O triplo de {número} é {triplo}")
print(f"A raiz quadrada de {número} é {square_root}")