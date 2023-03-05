import matplotlib.pyplot as plt
import math
from decimal import *

# set decimal precision
getcontext().prec = 256

plotx = [x for x in range(200, 1000)]
ploty = []

for x in plotx:
    res = Decimal(0)
    for i in range(1, 107):
        res += (((Decimal(math.factorial(108)) / (Decimal(math.factorial(i)) * Decimal(math.factorial(108 - i)))) * (Decimal(-1)**Decimal(i + 1)) * Decimal(108-i)**Decimal(x)) / (Decimal(108)**Decimal(x)))
    ploty.append(Decimal(1) - res)

ployz = [0.95 for x in range(200, 1000)]

plt.scatter(plotx, ploty)
plt.plot(plotx, ployz, 'r--')
plt.show()