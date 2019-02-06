n1 = 1200
n2 = 3455
n3 = n1+n2
print "The sum of", n1, " and", n2, " is",
print n3

print "The sum of %s and %s is %s" % (n1, n2, n3)
print "The sum of {0} and {1} is {2}".format(n1, n2, n3)

# __name__ refers to the module under execution and will have
# __main__ as the module name for the file supplied to python command
print("__name__ is " + __name__)

