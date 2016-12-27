print "Type the filename again:" # remind to type
file_again = raw_input("> ") # type the filename again and pass the value to file_again

txt_again = open(file_again) # a process of open a file

print txt_again.read() # read the content of the file after open it