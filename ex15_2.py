from sys import argv # import argument variable

script, filename = argv # unpack the argument variable into two variables

txt = open(filename) # a process of open a file, receive argument 
# and return a file object

print "Here's your file %r:" % filename # print the name of the file
print txt.read() # read the content of the file after open it