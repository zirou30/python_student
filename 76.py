usuarios_banidos = ['joão', 'renata', 'gabriela']
super_usuario = 'mochileiro das galáxias'
sysadmin = 'root'

if super_usuario not in usuarios_banidos:
    print(super_usuario.title() + ', você já pode enviar sua resposta agora.')
    if 'root' in sysadmin:
        print('\n' + sysadmin.title() + ', você já pode enviar sua resposta agora.')
else:
    print("Você não possui permissão para enviar resposta")

'''
Caso o super_usuario não esteja(not in) na lsita de usuário_banidos(True)
executa o bloco de instrução..

Caso 'root' esteja(in) na lista de sysadmin(True) executa o bloco
de instrução.
'''