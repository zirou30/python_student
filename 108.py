lista_vazia = []    #Criado a lista vazia

for x in range(30): #Início do loop para criar os 30 itens
    lista_nova = {'cor': 'verde', 'pontos': 3, 'velocidade': 'media'}
    lista_vazia.append(lista_nova)  #Usado append para adicionar a lista vazia

for a in lista_vazia[:5]:   #Feito o fatiamento para exibir apenas os 5 primeiros itens
    print(a)

print('\nTotal da lista: ' + str(len(lista_vazia)))     #Usado função len() para exibir o total

'''
feito o loop for x craindo o dicionário com os 30 itens e
usado a função append para armazenar os resultados na
lista vazia. Criado outro loop para mostrar apenas o
5 primeiros e por usando a função len para exibir
o número total da lista.
'''
