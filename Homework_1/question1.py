from HW1_src import Linear_Function
from HW1_src import Quadratic_Function
from HW1_src import Cubic_Function 
import sys

for arg in sys.argv:
	try:
		if int(arg) == 1:
			print "The linear function was called: "
			Linear_Function(5000)
		if int(arg) == 2:
			print "The quadratic function was called: "
			Quadratic_Function(5000)
		if int(arg) == 3:
			print "The cubic function was called: "
			Cubic_Function(5000)
	except ValueError:
		if arg == "question1.py":
			pass
		else:
			print "Please either input 1, 2, or 3"
