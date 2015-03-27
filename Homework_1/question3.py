from HW1_src import Binary_Third 
import sys

for arg in sys.argv:
	try:
		print "Searchg for %s" % (int(arg))
		Binary_Third(int(arg))
	except ValueError:
		if arg == "question3.py":
			pass
		else:
			print "Pleas input a number"
