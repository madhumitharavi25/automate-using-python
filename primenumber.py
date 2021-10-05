# Python3 program to implement
# the above approach
from math import sqrt

# Function to find all prime
# numbers in the range [1, N]
def SieveOfEratosthenes(N):
	
	# isPrime[i]: Stores if i is
	# a prime number or not
	isPrime = [True for i in range(N + 1)]

	isPrime[0] = False
	isPrime[1] = False

	# Calculate all prime numbers up to
	# Max using Sieve of Eratosthenes
	for p in range(2, int(sqrt(N)) + 1, 1):
		
		# If P is a prime number
		if (isPrime[p]):
			
			# Set all multiple of P
			# as non-prime
			for i in range(p * p, N + 1, p):
				
				# Update isPrime
				isPrime[i] = False
				
	return isPrime

# Function to count pairs of
# prime numbers in the range [1, N]
# whose difference is prime
def cntPairsdiffOfPrimeisPrime(N,M):
	
	# Function to count pairs of
	# prime numbers whose difference
	# is also a prime number
	cntPairs = 0
	
	
	# isPrime[i]: Stores if i is
	# a prime number or not

	isPrime = SieveOfEratosthenes(N)
	print(isPrime)
	#isPrime = SieveOfEratosthenes(M)

	# Iterate over the range [2, N]
	for i in range(2, N + 1, 1):
		
		# If i and i - 2 is
		# a prime number
		if (isPrime[i] and isPrime[i - 6]):
			
			# Update cntPairs
			cntPairs += 1

	return cntPairs

# Driver Code
if __name__ == '__main__':
	
	M = int(input())#lower limit
	N = int(input())#upper limit
	
	if ((M>=2 and M<=1000) and (N>M and N<=2000)):
		print(cntPairsdiffOfPrimeisPrime(N,M))
	else:
		print("No Prime Pairs")

