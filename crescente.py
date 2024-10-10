print('Digite dois numeros:')
x = int(input())
y = int(input())

menor = 0

while x != y:
    if x < y:
        print('CRESCENTE')
    else: 
        print('DECRESCENTE')

    print('Digite dois numeros:')
    x = int(input())
    y = int(input())
