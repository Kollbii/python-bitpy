import matplotlib.pyplot as plt
import numpy as np
  
def x(t):
    return ((t*t*t)/2 + 5*t + 20)
def y(t):
    return (2*t*t + 40)

t_list = np.linspace(0,120,num=100)

y_list = y(t_list)
x_list = x(t_list)

plt.figure(num=0,dpi=100)
plt.plot(x_list,y_list)
plt.title("Równanie toru")
plt.xlabel("oś X")
plt.ylabel("oś Y")
plt.show()
