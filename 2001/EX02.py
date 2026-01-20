texto = "roma me tem amor"

texto = texto.lower().replace(" ", "")
invertido = texto[::-1]

if texto == invertido:
    print("Sim")
else:
    print("Não")
