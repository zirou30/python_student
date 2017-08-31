def funcao_das_galaxias_mais_distante(primeiro_nome, segundo_nome, idade=''):
    astrogildo_variavel = {'primeiro': primeiro_nome, 'ultimo': segundo_nome}
    if idade:
        astrogildo_variavel['idade'] = idade
    return astrogildo_variavel

variavel_das_profundezas_dos_7_mares_kkkkk = funcao_das_galaxias_mais_distante('seila', 'racha cuca', idade=1000)
print(variavel_das_profundezas_dos_7_mares_kkkkk)

'''
na linha 3 verifica a condição de idade se for vazia
executa o bloco 4 e 5
'''