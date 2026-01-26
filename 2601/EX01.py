import pandas as pd

# Usuário informa o nome do arquivo CSV
nome_arquivo = input("Digite o nome do arquivo CSV: ")

try:
    # Lê o arquivo CSV
    df = pd.read_csv(nome_arquivo)

    # Calcula a média e o máximo da coluna tempo_execucao
    media = df["tempo_execucao"].mean()
    maximo = df["tempo_execucao"].max()

    # Exibe os resultados
    print(f"Média do tempo de execução: {media}")
    print(f"Maior tempo de execução: {maximo}")

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")

except KeyError:
    print("Erro: a coluna 'tempo_execucao' não existe no arquivo.")

except Exception as erro:
    print("Erro ao ler o arquivo CSV.")
    print("Detalhes:", erro)
