from datetime import date

# Entrada de dados
ano = int(input("Digite o ano de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
dia = int(input("Digite o dia de nascimento: "))

# Data de nascimento
data_nascimento = date(ano, mes, dia)

# Data atual
data_hoje = date.today()

# Cálculo dos dias
dias_vivo = (data_hoje - data_nascimento).days

# Saída
print("Você está vivo há", dias_vivo, "dias.")
