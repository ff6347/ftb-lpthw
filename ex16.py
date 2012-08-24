# -- coding: utf-8 --
#ex16.py

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that to happen hit CTRL-C (^C)."
print "If you want to do that hit RETURN (or ENTER ;))"

raw_input("Do it or dont?")

print "Opening the file %r. if it does not exist i will create it" % filename
target = open(filename, 'w')

print "Truncating %r. Goodbye" % filename

target.truncate()

print "Now you can add some text."
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "Witing to file"

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print "Closing file. Its like saving"

target.close()
separator = "------------------\n"
print "What follows is your files content"
print separator * 3

source = open(filename)
print source.read()

print separator * 3
