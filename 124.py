contador = 0

while contador <= 10:
    contador += 1
    if contador % 2 == 0:
        continue

    print(contador)

'''
usando a função continue if se o resto da divisão
por 2 for igual a 0, usando continue ele ignora o resto
do loop e retorna para o início e executa o print.
'''