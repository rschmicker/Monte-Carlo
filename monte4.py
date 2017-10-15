#!/usr/bin/env python
import math
import random

n = 1000
ctr = 0

results = {
	'2':0,
	'3':0,
	'4':0,
	'5':0,
	'6':0,
	'7':0,
	'8':0,
	'9':0,
	'10':0,
	'11':0,
	'12':0,
}

for i in range(n):
	roll1 = random.randint(1,6)
	roll2 = random.randint(1,6)
	total = roll1 + roll2
	results[str(total)] += 1
print(results)
