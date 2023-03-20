from random import randint
def throw_dice(number):
	result = {}
	for i in range (number):
		sum_values = randint (1,6) + randint (1,6)
		if sum_values in result:
			result [sum_values] += 1
		else:
			result [sum_values] = 1
	return result