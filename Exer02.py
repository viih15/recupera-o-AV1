# Faça um algoritmo que pergunte ao usuário quantos anos ele tem, depois disso, escreva True no console, caso ele já tenha alcançado a maioridade (18 anos), caso contrário escreva False.

#solicita ao usuario sua idade
idade = int(input("Quantos anos você tem?"))


#Verifica se o usuário ja alcançou a maioridade
maioridade = idade>= 18

#Escreve true ou false no console
print (maioridade)