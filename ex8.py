formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one"
	,"two","three","four")
print formatter % (False,True,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"This looks like",
	"JSON",
	"but it isnt",
	"JSON"
	)