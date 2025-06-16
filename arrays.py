from array import array

letras = ['a','b','c','d','e']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 1.4, 1.6, 1.8]

print(letras)
print(numeros_i)
print(numeros_f)

letras = array('u',['a','b','c','d','e'])
numeros_i = array('i',[10, 20, 30, 40])
numeros_f = array('f',[1.2, 1.4, 1.6, 1.8])

print(letras)
print(numeros_i)
print(numeros_f)