#!/usr/bin/env python
import math
import random

inside = 0
rolls = 10000
roll_dict = {
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
				'12':0
			}
for i in range(rolls):
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	total = d1 + d2
	key = str(total)
	roll_dict[key] += 1

for i in range(2,13):
	percent = float(roll_dict[str(i)])/float(rolls) * 100
	print(str(i) + ":\t" + str(percent))

print("Won " + str(float(roll_dict['7'])/float(rolls) * 100) + "% of " + str(rolls) + " rolls")
