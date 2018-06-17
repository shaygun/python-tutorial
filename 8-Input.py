
# Example 1
print "How old are you?",
age = raw_input()
print "So, you're %r old." % (age)
==> So, You're '38' old.

# Example 2
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
==>So, you're '38' old, '6\'2"' tall and '180lbs' heavy.

# Example 3 (argument passing)
from sys import argv
script, first, second, third = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
==>python ex13.py first 2nd 3rd
==>The script is called: ex13.py
==>Your first variable is: first
==>Your second variable is: 2nd
==>Your third variable is: 3rd

# Example 4 (argument passing)
import sys
print sys.argv[1] #only print the second argument
print = input('please enter the string you want to print: ')
python file.py "hello python"
