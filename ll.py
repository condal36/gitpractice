import numpy as np
import matplotlib.pylab as plt
def step_function(x):
    return np.array(x>0, dtype=np.int)
#fig=plt.figure(figsize=(4,3),facecolor='blue')
#plt.show()
x=np.arange(-5.0,5.0,0.1)
y=step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)

plt.subplot(221)
plt.plot(x, x)
plt.show()