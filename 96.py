chuck_noia = {'posicao_x': 0, 'posicao_y': 25, 'velocidade': 'media'}
print('Posição original x: ' + str(chuck_noia['posicao_x']))

if chuck_noia['velocidade'] == 'baixa':
    incrementa_x = 1
elif chuck_noia['velocidade'] == 'media':
    incrementa_x = 2
else:
    #Tá acelarado como um jato
    incrementa_x = 3

#A nova posição é a antiga posição mais o incrementa.
chuck_noia['posicao_x'] = chuck_noia['posicao_x'] + incrementa_x

print('A nova posicao x: ' + str(chuck_noia['posicao_x']))


'''
e verificado a key velocidade do dicionário chuck_noia
de acordo com a sua velocidade, se foi criado uma nova variável
incrementa_x e na 13 e somado a sua antiga key com a nova variável
incremnta_x
'''