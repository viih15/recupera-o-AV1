 Faça um programa que solicite ao usuário sua idade, depois disso, exiba a classificação etária de acordo com as faixas de valores:
  
  # Solicita ao usuário sua idade
idade = int(input("Digite sua idade: "))

# Verifica a classificação etária
if idade < 13:
    classificacao = "Criança"
elif 13 <= idade <= 17:
    classificacao = "Adolescente"
elif 18 <= idade <= 64:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

# Exibe a classificação etária
print(f"Sua classificação etária é: {classificacao}")