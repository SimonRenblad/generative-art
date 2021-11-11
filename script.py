import random
import math
import matplotlib.pyplot as plt
from samila import GenerativeImage

def f1(x,y):
    result = y * math.cos(5*x)
    return result

def f2(x,y):
    result = x * math.sin(5*y)
    return result

g = GenerativeImage(f1,f2)
g.generate()
g.plot()
plt.savefig('test.png')
