pizza = {
    'tipo': 'borda recheada com catupiry',
    'recheios': ['quatro-queijo', 'cogumelos']
}

print('Seu tipo de pizza foi ' + pizza['tipo'] +
      ', com os recheios:')

for x in pizza['recheios']:
    print('\t' + x)

'''
iniciamos o dicionário com o tipo e os recheios no formato de lista linha 1
mostramos na tela linha 6 o seu tipo de pizza e na linha 9
iniciamos um loop for no dicionário pizza chamandos apenas 
o recheios
'''