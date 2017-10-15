#!/usr/bin/env python
import math
import random

n = 1000
xmin = 0
xmax = 1
ymin = 0
ymax = 2
zmin = 0
zmax = 3
ctr = 0

cube_area = (xmax - xmin) * (ymax - ymin) * (zmax - zmin)

for i in range(n):
	randx = random.uniform(xmin, xmax)
	randy = random.uniform(ymin, ymax)
	randz = random.uniform(zmin, zmax)
	if pow(randx,2) + (pow(randy,2)/4) + (pow(randz,2)/9) <= 1:
		ctr += 1

area = float(cube_area) * (float(ctr)/float(n))
print(area)
