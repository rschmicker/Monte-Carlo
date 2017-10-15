#!/usr/bin/env python
import math
import random

n = 1000
xmin = 0
xmax = 2
ymin = 0
ymax = 65
ctr = 0

rect_area = (xmax - xmin) * (ymax - ymin)

for i in range(n):
	randx = random.uniform(xmin, xmax)
	randy = random.uniform(ymin, ymax)
	if randy <= (math.exp(pow(randx, 2))):
		ctr += 1

area = float(rect_area) * (float(ctr)/float(n))
print(area)
