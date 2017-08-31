def funcao_para_dicionario(hackudos, kidies):   #criado a funcao com 2 argumentos
    '''Criado a variavel abaixo atribuindo a ela um dicionário'''
    variavel_pode_ser_o_que_voce_quiser = {'hackudo': hackudos.title(), 'noobs': kidies.title()}
    return variavel_pode_ser_o_que_voce_quiser  #retornando seu valor

'''Criado a variavel abaixo e dado os valores dos argumentos da funcao '''
nasa = funcao_para_dicionario('kevin mitnick', 'aqueles que nao sabem programar')
print('O hacker que entrou para história ' + nasa['hackudo'] + '\n'
      'e os noobs são ' + nasa['noobs'] + '.')  #mostra na tela
