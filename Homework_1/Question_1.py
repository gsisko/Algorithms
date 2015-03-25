#imports
from datetime import timedelta
from datetime import datetime

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




#test Output for homework
input = 5000
Linear_Function(input)
Quadratic_Function(input)
Cubic_Function(input)

