peso = float(input("Digite seu peso (kg) :" ))
altura = float(input("Digite sua altura (M): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    classificao = "Abaixo do peso"
elif imc < 25:
    classificao = "Peso normal"
elif imc < 30:
    classificao = "Sobrepeso"
print(f"Seu IMC é {imc:.2f} - {classificao}")