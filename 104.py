linguagens = {
    'joao': 'python',
    'renata': 'ruby',
    'gabriela': 'lisp',
    'pedro': 'html',
    'os_goonies': 'python + django'
}

for nomes in sorted(linguagens.keys()):
    print(nomes.title() + ', sua linguagem favorita e ' + linguagens[nomes])

'''
Usado a função built-in do python chamada sorted
para organizar por ordem alfabética as keys()
do dicionário.
'''
