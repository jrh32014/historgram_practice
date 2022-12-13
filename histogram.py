Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from matplotlib import as plt
SyntaxError: invalid syntax
>>> from matplotlib import pyplot as plt
>>> import numpy as np
>>> fig,ax = plt.subplots(1,1)
>>> a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
>>> ax.hist(a, bins = [0,25,50,75,100])
(array([ 5.,  3.,  5.,  2.]), array([  0,  25,  50,  75, 100]), <a list of 4 Patch objects>)
>>> ax.set_title("histogram of result")
<matplotlib.text.Text object at 0x070A7B30>
>>> ax.set_xticks([0,25,50,75,100])
[<matplotlib.axis.XTick object at 0x06F29CB0>, <matplotlib.axis.XTick object at 0x06D691F0>, <matplotlib.axis.XTick object at 0x070DEA10>, <matplotlib.axis.XTick object at 0x070DEC30>, <matplotlib.axis.XTick object at 0x070DEEB0>]
>>> ax.set_xlabel('marks')
<matplotlib.text.Text object at 0x06F0E350>
>>> ax.set_ylabel('no.of students')
<matplotlib.text.Text object at 0x06F0EF50>
>>> plt.show()
>>> 
