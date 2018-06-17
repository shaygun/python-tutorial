## Functions

## Example 1
def print_two(*args): # this one is like your scripts with unlimited args and put them in list
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2): # this just takes one argument
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_none():
    print_two("Zed","Shaw")
    print_two_again("Zed","Shaw")

## Example 2
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
age = add(30, 5)
print (age)

## Example 3
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

## Example 4 (Global - Namespace)
def my_first_function(x, *args):  # *args means optional value, #args is tuple
    print(x) #*args is just a name, it can be anything as long as we use * before the name
    print(args)
    global my_var  #refer to global namespace not in the function
    print(my_var)
my_var = 2
my_first_function("test", "test2")
my_first_function("test", "test2", "test3", "test4")
