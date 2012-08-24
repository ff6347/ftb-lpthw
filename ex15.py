# -- coding: utf-8 --
#ex15.py
#reading files finally

from sys import argv

script, filename = argv

txt = open(filename)  # this looks easy

print "Here's your file %r:" % filename
print txt.read()

print "Type your filename again:"
file_again = raw_input(">>> ")
txt_again = open(file_again)

print txt_again.read()

print "Well Done. I will close the files now"

txt_again.close()
txt.close()
