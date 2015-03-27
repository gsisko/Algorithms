from math import floor

#Question 3

def Binary_Third(K):
	domain  = range(2,202,2)
	lower = 0
	upper = 100
	oldsearch = 0
	search = lower + int(floor((upper-lower)/3))
	comparisons = 0

	while domain[search] != K:
		search = lower + int(floor((upper-lower)/3))
		print search
		if oldsearch == search:
			print 'K was not found in the Domain'
			break
		elif domain[search] > K:
			comparisons += 1
			upper = search-1
		elif domain[search] < K:
			comparisons += 1
			lower = search+1
		elif K == domain[search]:
			comparisons += 1
			print "Found K at index %s after %s comparisons" % ( search, comparisons)
			break
		oldsearch = search


#Testing
"""
for i in range(0,201):
	print "Searching for " + str(i)
	Binary_Third(i)
"""

