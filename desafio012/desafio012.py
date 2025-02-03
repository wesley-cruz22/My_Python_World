"""
Faça um algoritmo que lê o preço de um produto e mostre seu novo preço com 5$ de desconto

# Você também pode fazer desta forma: 
novo_preço = (produto - (produto * 0.05)) # Macete ensinado pelo professor! 
novo_preço = produto - (produto * 5 / 100) # Outra maneira de fazer o calculo! 
"""
# Primeira forma de resolução
produto = float(input("Qual é o preço do produto: R$"))
novo_preço = produto - (produto * 0.05) # Outra maneira de declarar o 5%

print(f"O preço do produto era {produto:.2f}. O novo preço do produto com o desconto de 5% é {novo_preço:.2f}")

