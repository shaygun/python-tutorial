## example 1
print "." * 10
==> ..........

## example 2
end1 = "A"
end2 = "B"
end3 = "C"
end4 = "D"
end5 = "E"
end6 = "F"
print end1 + end2 + end3,
print end4 + end5 + end6
==> ABC DEF

## example 3
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ", days
print "Here are the months: ", months
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even4linesifwewant,or5,or6.
"""
==> Here are the days: Mon Tue Wed Thu Fri Sat Sun Here are the months: Jan
==> Feb
==> Mar
==> Apr
==> May
==> Jun
==> Jul
==> Aug
==> There's something going on here.
==> With the three double-quotes.
==> We'll be able to type as much as we like.
==> Even 4 lines if we want, or 5, or 6.

## example 4 (Escape Charecter)
print('we\'re going to the store') #scape charecter

## example 5 (Concatination)
print ('Hi', 'there') #Out: Hi there #it will add space
print ('Hi'+'there') #Out: Hithere
print ('Hi', '5') #Out: Hi 5
print ('Hi ' + str(5)) #Out: Hi 5
print ('Hi' + 5) #this is wrong

print("I don't like ", end="")  # new string wont be printed in new line, it will be at end of each other
print("newlines")

print('\n' * 5) #it will repeat new line 5 time
test = "cisco"
print ("b" not in test) #bring back true or false if charected is there
