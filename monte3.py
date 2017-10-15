#!/usr/bin/env python
import math
import random

n = 1000
ctr = 0

results = {
	'1':0,
	'2':0,
	'3':0,
	'4':0,
	'5':0,
	'6':0,
}

for i in range(n):
	roll = random.randint(1,6)
	results[str(roll)] += 1
print(results)
