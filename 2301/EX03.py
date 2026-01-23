import requests

cep = input("Digite o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()  # Verifica erro HTTP

    dados = resposta.json()

    # Verifica se o CEP existe
    if "erro" in dados:
        print("❌ CEP não encontrado.")
    else:
        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")

        print("\nInformações do CEP:")
        print("Logradouro:", logradouro)
        print("Bairro:", bairro)
        print("Cidade:", cidade)
        print("Estado:", estado)

except requests.exceptions.RequestException:
    print("❌ Falha na requisição. Verifique sua conexão e tente novamente.")
