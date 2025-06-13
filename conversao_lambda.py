#def cubo(num):
#    return num ** 3

cubo = lambda num: num**3 #parametro e expressão

user_number = int(input('Digite um número: '))
print(f'O cubo do número {user_number} é {cubo(user_number)}')
