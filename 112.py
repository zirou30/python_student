dic = {
    'n1': {
        'primeiro_nome': 'joão',
        'ultimo_nome': 'seila',
        'localizacao': 'vietnã'
    },
    'n2': {
        'primeiro_nome': 'renata',
        'ultimo_nome': 'naofacoIdeia',
        'localizacao': 'faixa de gaza'
    }
}

for nomes, info in dic.items():
    print('\nUsuario:' + nomes)
    nome_completo = info['primeiro_nome'] + ' ' + info['ultimo_nome']
    localizacao = info['localizacao']
    print('\tNome completo: ' + nome_completo.title())
    print('\tLocalizacao: ' + localizacao.title())

'''
Criado os dicionários da linha 1 ao 12
depois e feito o loop for usando .items
depois concatenando cada item a seus respectivos lugares.
'''