#def multi(num1,num2):
#    return num1 * num2

multi = lambda num1, num2: num1 * num2
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print(f'A multiplicação dos números {num1} e {num2} é {multi(num1,num2)}')