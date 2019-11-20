#3x1-x2+2x3+x4=16
#x1 - 4x2 -x3 +2x4 = 1
#-2x1 + x2 + 5x3 -2x4 = 17
#x1-2x2+x3-4x4=11

import math
import matplotlib.pyplot as plt
import decimal as de

de.getcontext().prec = 5
iteracii = [0]
x1 = [0]
x2 = [0]
x3 = [0]
x4 = [0]

def presmetaj_x1(x2, x3, x4):
    x1 = float (de.Decimal(16 / 3 + x2 / 3 + 2 * x3 / 3 + x4 / 3) )
    return x1

def presmetaj_x2(x1, x3, x4):
    x2 = float (de.Decimal(x1 / 4 - x3 / 4 + x4 / 2 - 1 / 4) )
    return x2

def presmetaj_x3(x1, x2, x4):
    x3 = float (de.Decimal(17 / 5 + 2 * x1 / 5 + x2 / 5 - 2 * x4 / 5) )
    return x3

def presmetaj_x4(x1, x2, x3):
    x4 = float (de.Decimal(x1 / 4 - x2 / 2 + x3 / 4 - 7 / 4) )
    return x4

e = 1
i = 1

while(e>0.01):
    x1.append(presmetaj_x1(x2[i - 1], x3[i - 1], x4[i - 1]))
    x2.append(presmetaj_x2(x1[i - 1], x3[i - 1], x4[i - 1]))
    x3.append(presmetaj_x3(x1[i - 1], x2[i - 1], x4[i - 1]))
    x4.append(presmetaj_x4(x1[i - 1], x2[i - 1], x3[i - 1]))
    iteracii.append(i)
    a=x1[i]-x1[i-1]
    b=x2[i]-x2[i-1]
    c=x3[i]-x3[i-1]
    d=x4[i]-x4[i-1]
    e = float(de.Decimal(math.sqrt( a*a + b*b +c*c + d*d )))
    i += 1
    

    
    

plt.plot(iteracii, x1, label='x1')
plt.plot(iteracii, x2, label='x2')
plt.plot(iteracii, x3, label='x3')
plt.plot(iteracii, x4, label='x4')
    
plt.xlabel('broj na iteracii')
plt.ylabel('x1 | x2 | x3 | x4')

plt.title("Metod na Jakobi")

plt.legend()

plt.show()