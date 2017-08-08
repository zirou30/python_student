linguagens = {
    'joao': 'python',
    'renata': 'ruby',
    'gabriela': 'html'
}

nomes = ['astrogildo']

for chaves in linguagens.keys():
    print(chaves)

if chaves not in nomes:
    print('' + nomes[0] + ' você sabe programar?')

'''
usando if na variável chaves e junto foi utilizado not in
se na variável chaves não tiver(not in) na variável nomes
continua o bloco de instrução.
'''