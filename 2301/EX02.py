import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()  # verifica erro HTTP

    dados = resposta.json()

    usuario = dados["results"][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Usuário fictício gerado:")
    print("Nome:", nome)
    print("E-mail:", email)
    print("País:", pais)

except requests.exceptions.RequestException:
    print("❌ Falha ao conectar com a API. Tente novamente mais tarde.")
