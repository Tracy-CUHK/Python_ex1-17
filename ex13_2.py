from sys import argv

script, age, height, weight = argv

print "The script is called:", script

age = raw_input ("please input your age:")
height  = raw_input ("please input your height:")
weight = raw_input ("please input your weight:")

print "The script is called:", script
print "Your first variable is: %r" % age
print "Your second variable is: %r" % height
print "Your third variable is: %r" % weight