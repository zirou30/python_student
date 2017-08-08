linguagens = {
    'astrogildo': 'lisp',
    'gabriela': 'ruby',
    'renata': 'python'
}
nomes = ['astrogildo', 'renata']

for nome in linguagens.keys():
    print(nome.title())

    if nome in nomes:
        print('Opa ' + nome.title() +
              ', sua linguagem favorita é ' +
              linguagens[nome].title() + '!')

'''
usa .keys() para pegar a chave do dicionario linguagens
com for percorrer o dicionário pegando apenas sua chaves
com .keys() é depois if verifica nome na lista nomes se
ele se encontra e sim continua o loop.
'''