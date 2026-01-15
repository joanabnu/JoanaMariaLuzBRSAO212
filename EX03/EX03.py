valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro
print(f"Valor em reais: R$ {valor_reais:.2f}")
print("Valor em dólares: $", round(valor_dolar, 2))
print(f"Valor em euros: € {valor_euro:.3f}")