# -- coding: utf-8 --
#ex15_1.py

from sys import argv  # import stuff for arguments

script, newfilename = argv  # now set some variables

txt = open(newfilename, 'w')  # open text file for writing

  # User input for file
mystring = raw_input("Type something for the new file: ")

txt.write(mystring)  # wirte to file

txt.close()

#now reopen the file for reading
print "This is your %s new content" % newfilename
newtxt = open(newfilename, "r")
print newtxt.read()

print "Well Done. I will close %s " % newfilename

newtxt.close()
