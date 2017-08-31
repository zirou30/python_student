def funcaoDequalquerPorra(nome, ultimo):
    seu_nome_completo_armazenado_nessa_variavel_seu_FDP = nome + ' ' + ultimo
    return seu_nome_completo_armazenado_nessa_variavel_seu_FDP.title()

while True:
    print('Bem-Vindo terráqueo')
    print('digite q para sair')
    p_nome = input('Digite seu primeiro nome: ')
    if p_nome == 'q':
        break
    u_ultimo = input('Digite seu sobrenome: ')
    if u_ultimo == 'q':
        break

    seu_nome_completo_humano_da_raca_inferior = funcaoDequalquerPorra(p_nome, u_ultimo)
    print('Olá terráqueo ' + seu_nome_completo_humano_da_raca_inferior + '\n')

'''
nas linhas 9 e 12 verifica se a letra digita corresponde a correta para sair
caso seja o programa para caso não ele vai executa o loop while infinitamente
e mostra na tela seu resultado.
'''
