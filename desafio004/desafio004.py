"""
Faça um programa que lê algo pelo teclado e mostre na tela o seu tipo primitivo 

OBS: Todo objeto String têm esses métodos
"""
caracter = (input("Digite algo: "))

# Verificando seu tipo primitivo
print(f"Qual é o seu tipo primito? {type(caracter)}")

 # Verifica se é alfabetico
print(f"É alfabetico? {caracter.isalpha()}")

# Verifica se é numérico
print(f"É numérico ? {caracter.isnumeric()}") 

# Verifica se é alfanumérico
print(f"É alfanumérico? {caracter.isalnum()}") 

# Verifica se é decimal
print(f"É um valor decimal? {caracter.isdecimal()}") 

# Verifica se está em letras maiúsculas
print(f"Está em letras maiúsculas? {caracter.isupper()}") 

# Verifica se está em letras minúsculas
print(f"Está em letras minúsculas? {caracter.islower()}") 

# Verifica se todos os digitos de uma String são numéricos(0-9) e se a String não é vazia
print(f"É um digito de valor númerico ou uma String vazia? {caracter.isdigit()}")

# Verifica se é um identificador
print(f"É um identificador? {caracter.isidentifier()}")

# Verifica se pode ser impresso no console(terminal)
print(f"Pode ser impresso? {caracter.isprintable()}")

# Compreende os caracteres com valores Unicode entre 0 e 127
print(f"Faz parte do conjunto ASCII? {caracter.isascii()}")

# Verifica se há apenas espaços em branco
print(f"Tem apenas espaços? {caracter.isspace()}") 

# Verifica se está capitalizada
print(f"Está capitalizada? {caracter.istitle()}")