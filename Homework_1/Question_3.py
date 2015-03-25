from math import floor

#Question 3

def Binary_Third(K):
	domain = range(2,200,2)
	lower = 2
	upper = 200
	range = 0
	oldsearch = 0
	search = 0	
	comparisons = 0

	while domain[search] != K:
		oldsearch = search
		search = floor(lower + ((upper-lower)/3)
		if domain[search] > K:
			comparisons += 1
			lower = search
		elif domain[search] < K:
			comparisons += 1
			upper = search
		elif K == search:
			comparisons += 1
			print('Found K at index %s after %s comparisons')
		elif oldsearch == search:
			print 'K was not found in the Domain'

#Testing
Binary_Third(100)

