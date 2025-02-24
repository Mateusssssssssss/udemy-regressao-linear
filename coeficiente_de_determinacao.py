#Calculo do coeficiente de determinação
#Ajuda na criação de modelos preditivos:
# se r > 0.7 Forte capacidade explicativa, ótimo para modelos preditivos 
# r 0.5 a 0.7 boa
# r 0.3 a <0.5  Moderada
# r abaixo de 0.3  Fraca capacidade explicativa
correlacao = 0.6437009222786095
r2 = correlacao ** 2
r = r2
print(r)
# Isso significa que cerca de 41,43% da variação no valor das vendas pode ser 
# explicada pelo número de novos clientes. O restante da variação pode 
# estar ligado a outros fatores, como promoções, sazonalidade 
# ou fidelização de clientes.