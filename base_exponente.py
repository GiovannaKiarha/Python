def potencia(base, expoente=2): #função
    return base ** expoente #calculo da 

base = int(input('Digite um número para a sua base:'))

expoente = input('Digite um número para ser o expoente(default 2):') # se converter para int aqui, vai ficar zero
    
if expoente:
    print(f'O resultado é: {potencia(base,int(expoente))}')
else:
    print(f'O resultado é: {potencia(base)}') # para caso não dê o número de expoente
