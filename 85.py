ingredientes = ['queijo', 'mussarela', 'cogumelos']

if 'queijo' in ingredientes:
    print('queijo adicionado'.title())

elif 'mussarela' in ingredientes:
    print('mussarela adicionado'.title())

elif 'cogumelos' in ingredientes:
    print('cogumules adicionados'.title())

'''
Quando se tem a primeira condição verdadeira, python não roda
o bloco de if-elif-else. Se deseja que os outros blocos sejam
executado use uma série de if independentes.
'''
