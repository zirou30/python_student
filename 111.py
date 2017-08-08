linguagens = {
    'joão': ['python', 'ruby'],
    'renata': ['java'],
    'gabriela': ['assembly', 'c'],
    'astrogildo': ['lisp', 'haskell']
}

for chaves, valores in linguagens.items():
    print('' + chaves.title() + ' suas linguagens favoritas são:')
    for linguagem in valores:
        print('\t' + linguagem.title())

'''
com loop for definimos dois valores chaves e valores
então pegamos ambos os valores com a função .items()

'''
