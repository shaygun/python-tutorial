## Formatted Output (Format String, Formatter)
%s - String (or any object with a string representation, like numbers)
%d - Integers/Digit
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

## example 1
my_name = 'Zed A. Shaw'
print "Let's talk about %s." % my_name
==> Let's talk about Zed A. Shaw.

## example 2
my_eyes = 'Blue'
my_hair = 'Brown'
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
==> He's got Blue eyes and Brown hair.

## example 3
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
==> If I add 35, 74, and 180 I get 289.

## example 4
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

## example 5
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
==> Isn't that joke so funny?! False

## example 6
formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
==> 1 2 3 4
==> 'one' 'two' 'three' 'four'
==> True False False True
