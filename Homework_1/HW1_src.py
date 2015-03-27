#imports
from datetime import timedelta
from datetime import datetime
from math import floor

#Question 1 

#Part A
def Linear_Function(n):
	"""Function that runs as O(n), using one loop
	"""
	begin = datetime.now()	#record start time
	Sum = 0
	for i in xrange(n):
		Sum += 1

	end = datetime.now()    #record end time
	duration = end - begin	#subtract to find duration as a time delta
	#Print timedelta object
	print duration


#Part B
def Quadratic_Function(n):
	"""Function that runs in O(n^2)  time, using two loops
	"""
	begin = datetime.now()	#record start time
	Sum = 0
	for i in xrange(n):
		for j in xrange(n):
			Sum += 1

	end = datetime.now()    #record end time
	duration = end - begin	#subtract to find duration as a time delta
	#Print timedelta object
	print duration

#Part C

def Cubic_Function(n):
	"""Function that runs in O(n^3)  time, using three loops
	"""
	begin = datetime.now()	#record start time
	Sum = 0
	for i in xrange(n):	#xrange is used in order to save on memory
		for j in xrange(n):
			for v in xrange(n):
				Sum += 1

	end = datetime.now()    #record end time
	duration = end - begin	#subtract to find duration as a time delta
	#Print timedelta object
	print duration

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






