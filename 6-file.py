
## Read file
## Example 1
from sys import argv
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
==> python ex15.py ex15_sample.txt

## Write file
## Example 2
from sys import argv
script, filename = argv
print "We're going to erase %r." % filename
raw_input("?")
print "Opening the file..."
target = open(filename, 'w')
target.truncate()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it."
target.close()

## Example 3
import sys
import os
test_file = open("test.txt", "wb") #r for reading, w writing, a appending(it will not delete the current file data), b binary format(exe,pdf),,
print(test_file.mode)  #read and write the file at same time is w+
print(test_file.name)
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()

test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)

text_in_file = test_file.readline() # read the file line by line
print(text_in_file)

text_in_file.seek(0) #it will go back to begning of the file to b read
text_in_file.tell() #it will show 0
text_in_file = test_file.read(5) #return first 5 charecter
print(text_in_file)

os.remove("test.txt")

myfile.seek(0) #this code will check the file and show those line start with A
for line in myfile.readlines():
   if line.startwith("A"):
         print line


################################ PICKLE ##############################################
import pickle

## Add this to your code , change variable_example_or_list to the variable
############ DEBUG TO FILE ############
        with open('/testrun/output.pkl', 'wb') as fp:
            pickle.dump(variable_example_or_list, fp)
############ DEBUG TO FILE ############

## Seperate file
############ Read the Dump ############
import pickle
# read python dict back from the file
pkl_file = open('output.pkl', 'rb')
mydict = pickle.load(pkl_file)
pkl_file.close()
print mydict
############ Read the Dump ############
################################ PICKLE ##############################################
