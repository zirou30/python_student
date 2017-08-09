mensagem = ''
sair = '\nsair para encerrar o programa:'

while mensagem != 'sair':
    mensagem = input('Digite sua mensagem ao mundo térraqueo, ' + sair)
    print(mensagem)

'''
Ele fica num loop eterno enquanto a mensagem 
digitada não seja sair.
'''