#!/usr/bin/python
#This program gives the random number

import time

def random():
	valueList = []
	counters = [0,0]
	randomDiff = 0

	for i in range(100):
		seed = time.time()
    		decimalVal = str(seed).split('.')
    		val = (int(decimalVal[1])+randomDiff)%10
    		if val == 0:
        		val += 1
    		if counters[0]>=49 and val<=5:
        		val +=5

    		elif counters[1]>=51 and val>5:
        		val -=5

    		if val<=5:	
			counters[0]+=1
    		else:
        		counters[1]+=1
    		multiplier = (int(decimalVal[1])%7)
    		randomDiff += int(decimalVal[1])*multiplier
    		time.sleep(0.1)
    		valueList.append(val)

	print counters
	print valueList

random()
