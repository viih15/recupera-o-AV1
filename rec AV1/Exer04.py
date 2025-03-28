faça um algoritmo que solicite 3 notas para o usuário, calcule a média e indique se o aluno foi aprovado ou reprovado (nota precisar ser maior ou igual à sete para o aluno ser aprovado) 

#solicita 3 notas ao usuario
nota1 = float (input("digite a primeira nota:"))
nota2 = float (input("digite a segunda nota:"))
nota3 = float (input("digite a terceira nota:"))
 
#calcule a media das notas 
media = (nota1+nota2+nota3) /3

#verifica se o aluno foi aprovado ou reprovado
if media >=7:
        print (f"media: {media:.2f} - aluno aprovado!") 
else:
        print (f"media: {media:.2f} - aluno reprovado.") 
