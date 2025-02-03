"""
Crie um programa que lê quanto dinheiro a pessoa tem na carteira e mostre quantos dólares ela pode comprar
"""
# Entrada de dados 
carteira = float(input("Quanto dinheiro você tem na carteira? R$"))
dólar_hoje = float(input("Qual a cotação do dólar atualmente? R$"))

comprar = carteira / dólar_hoje

print(f"Com R${carteira:.2f} você pode comprar U${comprar:.2f}")