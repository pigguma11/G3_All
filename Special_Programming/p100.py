def func(x):
    return 0.01*x**2+0.1*x

import numpy as np
import matplotlib.pylab as plt

x=np.arange(.0, 20., .1)
y=func(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,y)
plt.show()

def numerical(f,x):
    h=1e-4
    return(f(x+h)-f(x-h))/(2*h)

print(numerical(func,5))
print(numerical(func,10))