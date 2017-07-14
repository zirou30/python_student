a = 'Python é 'legal''  #Tem uma aspa simples no final da string por isso o error ocorrer
b = "Python é "legal""  #Tem uma aspa duplas no final da string por isso o error ocorrer
print(a)
print(b)

'''
O error ocorre devido a mais uma aspa no final da string.
o correto seria:
a = 'Python é "legal"'
b = "Python é 'legal'"

Se vc coloca uma string dentro de aspas simples é quer destacar algo dentro
com aspas é necessário colocar aspas duplas. Pois se colocar simples o error 
de sintáxe inválida vai ocorrer, isso serve para aspas duplas
'''