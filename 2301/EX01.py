import random
import string

# Pede ao usuário o tamanho da senha
tamanho = int(input("Digite o tamanho da senha desejada: "))

# Conjunto de caracteres
letras = string.ascii_letters   # a-z e A-Z
numeros = string.digits         # 0-9
simbolos = string.punctuation   # símbolos

# Junta todos os caracteres
caracteres = letras + numeros + simbolos

# Gera a senha aleatória
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

# Exibe a senha
print("Senha gerada:", senha)
