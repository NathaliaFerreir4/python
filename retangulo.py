import math

base = float(input('Base do retangulo:'))
altura = float(input('Altura do retangulo:'))

area = 0
perimetro = 0
diagonal = 0

area = base * altura
perimetro = base * 2 + altura * 2
diagonal = math.sqrt(base**2 + altura ** 2)

print(f'AREA =  {area:.4f}')
print(f'PERIMETRO =  {perimetro:.4f}')
print(f'DIAGONAL = {diagonal:.4f}')