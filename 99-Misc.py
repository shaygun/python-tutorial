############################## id in memory ############################## 
a = 10
b = id(10) #this will give the address of 10 in memory
print(b)
print (id(a))
a = b
print (id(a)) #both of the variable will have same id number, since they are same
print (id(b))

############################## Type ##############################
var1 = "hello"
var2 = 10
var3 = 1.5
print (type(var3)) #show its type either int, float or string

############################## Conversion between data type ##############################
num = 2
flt = 2.5
num1 = str(num) #change number to string
type(num1)
flt1 = str(flt) #change float to string

str = "5"
str1 = int(str) #convert string to integer

num = 2 #convert integer to float
f = float(num)

tup1 = (1,2,3) #convert tuple to list
list1 = list(tup1)
tup = tuple(list1)

num = 10 #change inte to binary
num_bin = bin(num)

num_hex = hex(num)

bin_to_num = int(num_bin, 2) #binary to number
hex_to_num = int(num_hex, 16) #hex to number

############################## Python Module ##############################
touch my_module.py #both file should be in same directory
touch application.py
#my_module
my_var = 10
def my_function():
   print("This is the function inside the module")
print ("this will be executed")

#application
import my_module
#from my_module import my_var #only import this variable
print (my_module.my_var)
my_module.my_function()
