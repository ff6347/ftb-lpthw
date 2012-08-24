x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary,do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'" % y

hialrious = False
joke_eval = "Isn't that joke so funny?! %r" # %r takes raw data and can be embedded in a string
#thats wired

print joke_eval % hialrious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
