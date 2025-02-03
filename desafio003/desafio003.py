"""
Crie um programa que lê o nome e o salário de um funcionário, mostrando no final uma mensagem
"""
nome = str(input("Qual é o seu nome? ")).title().strip()
salário = float(input("Qual é o seu montante salarial? R$"))

print(f"O nome do funcionário é {nome}")
print(f"Seu montante salário é {salário:.2f}") # Ao fazer uso desses dois ponto, ponto final, 2 e f. Eu estou declarando quantas casas decimais deve me retornar como resultado