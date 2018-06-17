## If & Else

## Example 1
people = 30
cars = 40
buses = 15
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "Something Else"
else:
    print "test"

## Example 2
#if else elif == != > >= <= and or not
age = 21
if age > 16 :
    print('you are old enough to drive')
else :
    print ('you are not old enough')
if age >=21 :
    print ('you are old enough to drive a tractor trailer')
elif age >= 16:
    print('you are not old enough to drive car')
else : print('you are not old enough to drive')

if ((age>=1) and (age <= 18)):
    print("you get a birthday")
elif (age== 21) or (age>=65):
    print("you get a birthday")
elif not(age==30):
    print("you dont get a biarthday")
else:
    print("you get a birthday party")
