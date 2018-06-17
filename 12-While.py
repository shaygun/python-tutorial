## While
## while loop (used when you dont know how many time you need to run the loop)
## Example 1
i=0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
print "The numbers: "
for num in numbers:
    print num

## Example 2
i = 0
while True:
    i += 1
    if i == 12:
        break
    print (i)

## Example 3
while True:
    n = random.randint(0, 100)
    print(n)
    if n % 2 == 0:
        break

## Example 4
import random
random_num = random.randrange(0,100) #this will generate random number

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100) #it will change the random number

## Example 5
import random
random_num = 1
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100) #it will change the random number

## Example 6
i = 0;
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif(i == 9):
        break #it will tottaly jump out of while loop
    else:
        i += 1
        continue # jump back to while loop and start again #ignore the below code
    i += 1


    
