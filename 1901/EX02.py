
quantidade = int(input("Quantidade de alunos: "))
soma = 0

for i in range(quantidade):
    nota = float(input("Digite a nota do aluno: "))
    soma += nota

media = soma / quantidade
print(media)
