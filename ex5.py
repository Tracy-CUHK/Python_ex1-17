name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
transference_inch_cm = 2.54 # multiplication

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height,
	weight, age + height + weight)
print "I just want to add %d, %r, and %r." % (age, height, weight)
print "I want to tell you the color of my teeth is %r." % teeth
print "I want to tell you the color of my teeth is %s." % teeth
print "He's %r cm tall." % height * transference_inch_cm
