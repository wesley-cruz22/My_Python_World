"""
Crie um programa que lê uma distância em metros e mostre os valores relativos em outras medidas como:
Km -> quilometros
Hm -> hectometros
Dam -> decametros
cm -> centimetros
dm -> decimetros
mm -> milimetros
"""
metros = float(input("Digite uma medida em metros: "))

# Calculando a distância dos seus múltiplos
Km = metros / 1000
Hm = metros / 100
Dam = metros / 10

# Calculando a distância dos seus sub-múltiplos
dm = metros * 10
cm = metros * 100
mm = metros * 1000



# Exibindo a mensagem na tela
print(f"Km = {Km}Km")
print(f"Hm = {Hm}Hm")
print(f"Dam = {Dam}Dam")
print(f"dm = {dm}dm")
print(f"cm = {cm}cm")
print(f"mm = {mm}mm")