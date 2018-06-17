## Exceptions

## Example 1
for i in range(10): #if error happen it dont terminate the program,
    try:
        print i / 0
        except ZeroDivisionError:
            print "this is an error"
try:
    print 4 / 0
except ZeroDivisionError:
    print "not allowed"
finally:
    print "i dont care if an exception was raised"

## Example 2
(x,y) = (5,0)
try:
  z = x/y
except:
  print "divide by zero"
