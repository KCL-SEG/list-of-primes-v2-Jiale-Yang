"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
	list = []
	currentNum = 2
    
	if number_of_primes <= 0:
		raise ValueError

	while len(list) < number_of_primes:
		prime = True
		for i in range(2, currentNum):
			if currentNum % i == 0:
				prime = False
	
		if prime:
			list.append(currentNum)
		currentNum += 1
			
			
	return list
