
#! Média das notas

nota_1 = 10
nota_2 = 9
nota_3 = 8
nota_4 = 7

soma_das_notas = nota_1 + nota_2 + nota_3 + nota_4

media_das_notas = soma_das_notas/4

if media_das_notas <= 60:
    print("Suas notas são 1B(",nota_1,"), 2B(",nota_2,"), 3B(",nota_3,") e 4B(",nota_4,")\n Sua média é: ",media_das_notas,"\n\n")
    print("PARABÉNS APROVADO!!!")
else:
    print("Lamento você não atigiu a média 60, sua média foi de ",media_das_notas,"\n\n")
    print("REPROVADO ESTUDE MAIS!!!")