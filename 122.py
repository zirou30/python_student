men = True

while men:
    mensagem = input('Digite algo - quit para encerrar:')

    if mensagem == 'sair':
        men = False
    else:
        print(mensagem)

'''
E criado um while True na linha 3, enquanto a condição for
verdadeira ele vai estar sempre executando o loop. Quando
a condição se tornar False ele terminá o loop
'''