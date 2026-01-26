# Solicita o nome do arquivo ao usuário
nome_arquivo = input("Digite o nome do arquivo a ser lido: ")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        # Percorre cada linha do arquivo
        for linha in arquivo:
            print(linha.strip())

except FileNotFoundError:
    print("Erro: o arquivo não foi encontrado.")

except Exception as erro:
    print("Ocorreu um erro ao ler o arquivo.")
    print("Erro:", erro)
