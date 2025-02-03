"""
Crie um algoritmo que lê duas notas de uma aluno, calcule e moste a sua média
"""
materia = str(input("Digite aqui a sua matéria escolar: ")).title().strip()
nota_1 = float(input("Digite o valor da 1ª nota: "))
nota_2 = float(input("Digite o valor da 2ª nota: "))

# Calculando a média
média = (nota_1 + nota_2) / 2 # O 2 indica a quantidade de elementos que estão dentro dois parênteses

# Exibindo a mensagem final
print(f"A matéria informada pelo aluno foi {materia} e sua média nessa matéria é {média:.1f}")