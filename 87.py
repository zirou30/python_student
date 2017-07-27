ingredientes = ['queijo', 'tomate', 'calabresa']

for ingrediente in ingredientes:
    if ingrediente == 'tomate':
        print('Desculpa estamos sem ' + ingredientes[1])
    else:
        print('Adicionado ' + ingrediente + '.')
print('Pizza Pronta')
