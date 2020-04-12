# formulas
# semicirculo
# Perimetro = PI * radio
# R = Perimetro / PI
# Area = PI * R * R /2
# Despejando
# Area = Perimetro * Perimtro / 2 * pi
from math import pi

const = 1 / (2*pi)
while True:
    L = float(input())
    if L == 0: break
    print('%.2f' % (L * L * const))
