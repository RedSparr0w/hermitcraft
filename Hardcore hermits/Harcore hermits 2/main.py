#!/usr/bin/python
# -*- coding: latin-1 -*-
# This takes an input file in harcore hermits format (input.txt)

import numpy as np
import matplotlib.pyplot as plt
import math


with open('input.txt', 'r') as inFile:
    lines = []
    for i, line in enumerate(inFile):
        if i == 0:
            title = line.strip()
        elif i == 1:
            lines.append(line.strip().split('\t'))
        elif line.strip().split('\t') == ['###alive']:
            aliveLine = i-1
        else:
            lines.append(np.array([int(e) for e in line.strip().split('\t')]))
print(lines)

labels = lines[0]
y = np.transpose(lines[1:aliveLine])
x = np.transpose([i for i in np.arange(1, aliveLine)])
alive = np.transpose(lines[aliveLine:])*10

for i in range(len(y)):
    plt.plot(x, y[i], label=labels)
    plt.scatter(x, y[i], s=alive[i])

plt.title(title, size=16)
plt.xlabel('Episode')
plt.ylabel('Points')
plt.xlim(0, aliveLine)
plt.ylim(0, 10*math.ceil(np.max(y)*0.11))
plt.xticks(np.arange(0, aliveLine + 1, 1))
plt.legend(labels)
plt.savefig("Result.png")

#plt.show()