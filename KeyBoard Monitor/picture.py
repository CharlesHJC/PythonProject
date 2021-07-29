"""
 @Author:       CharlesHE 
 @Created:in:   2021/4/15.
 @Description:  
 @time: 2021/4/20 13:54
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

fp = open('key_stat.txt')
keys = []
stats = []
total = 0
for line in fp:
    x, y = line.split()
    x = x.replace('Key.', '').replace(':', '')
    keys.append(x)
    stats.append(int(y))
    total += int(y)
print(total)


plt.bar(keys, stats)
plt.xticks(keys, rotation='45')
plt.show()
