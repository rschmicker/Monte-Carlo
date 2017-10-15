#!/usr/bin/env python
import math
import random

insidepoints = 0
n = 10000000
for i in range(n):
	x = random.uniform(-1, 1)
	y = random.uniform(-1, 1)
	if (pow(x, 2) + pow(y, 2)) <= 1:
		insidepoints += 1

pi = 4*(float(insidepoints)/float(n))
print(pi)
