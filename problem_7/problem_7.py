"""
PROBLEM 7: 10001st prime
"""

import math

NTH_PRIME = 10001


"""
Checks if the number is prime or not checking if it can be divided by one of the previous primes already obtained
"""
def isPrime(number, list_of_previous_primes):
	#It has no sense to check the mod with those numbers that are higher than its square root
	number_sqrt = int(math.sqrt(number))

	""" 
	It is iterated over the list_of_previous_primes to check if the number is divisible by any of them
	Only those numbers smaller than the square root of the number are considered
	"""
	for x in list_of_previous_primes:
		if x > number_sqrt:
			#End of the loop, it is impossible to find a divisor from this point
			break
		if number % x == 0:
			#It is not prime as we found a divisor
			return False

	#If the loop has finished it means the number is prime
	return True

"""
It returns the nth prime number
"""
def obtainNthPrime():
	""" We will start the iteration from 3 as it is the first odd number, so if the one that it is requested to obtain is the 1st prime, it is returned 2 """
	if NTH_PRIME == 1:
		return 2

	n_primes_found = 1 #It is considered that we already have found 2
	list_of_previous_primes = [2] #The list of previous primes is initialized with 2

	next_number = 3
	"""
	The algorithm will finish once the nth prime is found
	For every prime number found, it is added to the list_of_previous_primes and increased the number of n_primes_found
	Only odd numbers will be considered, as no other even number apart from 2 will be prime
	"""
	while n_primes_found != NTH_PRIME:
		number = next_number
		#It is checked if is prime
		if isPrime(number, list_of_previous_primes):
			list_of_previous_primes.append(number)
			n_primes_found += 1

		next_number = number + 2 #Avoiding even numbers

	return int(number)

solution = obtainNthPrime()
print "Solution: " + str(solution)