from sys import argv # import argument variable

script, filename = argv # unpack the argument variable into two variables

txt = open(filename) # a process of open a file, receive argument 
# and return a file object

print "Here's your file %r:" % filename # print the name of the file
print txt.read() # read the content of the file after open it
txt.close()

print "Type the filename again:" # remind to type
file_again = raw_input("> ") # type the filename again and pass the value to file_again

txt_again = open(file_again) # a process of open a file

print txt_again.read() # read the content of the file after open it
txt_again.close()