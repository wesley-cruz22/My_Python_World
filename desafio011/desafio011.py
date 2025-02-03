"""
Faça um algoritmo que lê a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2m² 
"""
largura = float(input("Digite o valor da largura da parede em (m): "))
altura = float(input("Digite a altura da parede em (m): "))

# Calculando a área da parede
area = largura * altura

# Calculando a quantidade de tinta necessária
tinta_necessaria = area / 2

# Exibindo as mensagens na tela 
print(f"A área da parede mede {area:.2f}")
print(f"A quantidade de tinta necessária é {tinta_necessaria:.2f} litros")