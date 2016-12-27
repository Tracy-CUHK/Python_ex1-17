def add(a, b):
	print "ADDING %r + %r" % (a, b)
	return a + b
	
def subtract(a, b):
	print "SUBTRACTING %r - %r" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %r * %r" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %r / %r" % (a, b)
	return a / b
	
	
print "Let's do some math with just functions!"

arg1 = int(raw_input("argument1>> "))
arg2 = float(raw_input("argument2>> "))
arg3 = float(raw_input("argument3>> "))
arg4 = float(raw_input("argument4>> "))
what = add(arg1, subtract(divide(arg2, multiply(arg3, arg4)), arg4))

print "What becomes: ", what, "Can you do it by hand?"