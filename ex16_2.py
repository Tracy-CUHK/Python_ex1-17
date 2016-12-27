from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Open the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

summary = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(summary)

print "And finally, we save it."
target.close()

target_again = open(filename)
print target_again.read()

target_again2 = open("test.txt")
print target_again2.read()


