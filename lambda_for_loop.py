lista = [1, 2, 3, 4, 5, 6]

quadrado = lambda num: num ** 2

resultados = []

for i in lista:
    resultados.append(quadrado(i))

print(f'Os quadrados dos números {lista} são {resultados}')