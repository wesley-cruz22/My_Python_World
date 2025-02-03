"""
Faça um algoritmo que lê quanto dinheiro a pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar
"""
carteira = float(input("Quanto dinheiro você tem na carteira? R$"))
dólar = float(input("Quanto o dólar está valendo atualmente? R$"))

comprar = carteira / dólar

print(f"Com R${carteira:.2f} você pode comprar U${comprar:.2f}")
