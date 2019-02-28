import scipy.signal
import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('C:/Users/mango/Documents/readfromtxt/test.txt')
plt.plot(data[:,0],data[:,1])
plt.show()
#作图

print(data[:,0])
x=data[:,0]
y=[data[:,1]]
print(x, y)
#加不加[]区别
