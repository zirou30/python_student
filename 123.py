while True:
    pergunta = input('Lugares onde você visitou:' + '\n(sair para encerrar o programa)')

    if pergunta == 'sair':
        break
    else:
        print('Um bom lugar ' + pergunta.title())


'''
se a variável perguntar for diferente de sair o loop
continuará rodando. Quando for sair o mesmo encerrar o loop
'''