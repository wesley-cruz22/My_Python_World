"""
Faça um programa que lê as duas notas de um aluno em uma máteria e mostre na tela a sua média na disciplina
"""
materia = str(input("Digite o nome da matéria escolar: ")).strip()
nota_1 = float(input("Digite o valor da 1ª nota: "))
nota_2 = float(input("Digite o valor da 2ª nota: "))

média = (nota_1 + nota_2) / 2

print(f"A matéria informada pelo estudante foi {materia} e sua média nela foi {média:.1f}")