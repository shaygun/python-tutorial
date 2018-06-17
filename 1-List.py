#In Python programming, a list is created by placing all the items (elements)
#inside a square bracket [ ], separated by commas.

## List Example
my_list = []
my_list = [1, 2, 3] # list of integers
my_list = [1, "Hello", 3.4] # list with mixed datatypes
my_list = ["mouse", [8, 4, 6], ['a']] # nested list
my_list_test = [ ("test1"), ("test2")] # another example

## Negative indexing
my_list = ['p','r','o','b','e']
print(my_list[-1]) # Output: e
print(my_list[-5]) # Output: p

## Slice list
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[2:5]) # elements 3rd to 5th
print(my_list[:-5]) # elements beginning to 4th
print(my_list[5:]) # elements 6th to end
print(my_list[:]) # elements beginning to end
list[1:4] #it will take index 1 until 3
list[:3]  # show the first 3 items
list[3:] # start from index 3 and until the end
list[-1] #last element of the list from right to left
list[-3:] #it will show last 3 element of list
list[::2] # show second element only, start from 0 , 2, 4
list[::-1] #show all the element in reverse format

## Change or add elements to a list?
odd = [2, 4, 6, 8] # mistake values
odd[0] = 1 # change the 1st item
odd[1:4] = [3, 5, 7]   # change 2nd to 4th items

## Add element to list
odd = [1, 3, 5]
odd.append(7) # Output: [1, 3, 5, 7]
odd.extend([9, 11, 13]) # Output: [1, 3, 5, 7, 9, 11, 13]

odd = [1, 3, 5]
print(odd + [9, 7, 5]) # Output: [1, 3, 5, 9, 7, 5]
print(["re"] * 3) #Output: ["re", "re", "re"]

odd = [1, 9]
odd.insert(1,3) # Output: [1, 3, 9]
print(odd)

## Delete element in list
my_list = ['p','r','o','b','l','e','m']
del my_list[2] # Delete one item from list # Output: ['p', 'r', 'b', 'l', 'e', 'm']
del my_list[1:5] # delete multiple items # Output: ['p', 'm']
del my_list # delete entire list

my_list = ['p','r','o','b','l','e','m']
my_list.remove('p') # Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list.pop(1)) # Output: 'o'
print(my_list) # Output: ['r', 'b', 'l', 'e', 'm']
print(my_list.pop()) # Output: 'm'
print(my_list) # Output: ['r', 'b', 'l', 'e']
my_list.clear() # Output: []

## Other Example
grocery_list = ['juice', 'tomatoes', 'potatoes']
print('First Item', grocery_list[0]) #will print grocery_list
grocery_list[0]= "green juice"
print('First Item', grocery_list[0])
print(grocery_list[1:3]) #print index 1 and 2 only not 3
other_events = ['wash car', 'pickup kids', 'cash check']
to_do_list = [other_events, grocery_list] # 2 list inside each other
print(to_do_list)
print((to_do_list[1][1])) #second item of list 1 and 2
grocery_list.append('onions') #add this item to the end of the list
print(to_do_list)
grocery_list.insert(1, "pickle") #insert this item at index 1

## Deleting the item inside list
grocery_list.remove("pickle")
del grocery_list[4]
grocery_list.pop(0) # remove element 0
grocery_list.sort()
grocery_list.reverse()
print(len(to_do_list))
print(max(to_do_list)) #print the longest string or biggest number
print(min(to_do_list))
print(len(to_do_list)) #show how many element are in the list

## Other functions
list1.extend(list2) #it will mix both list to one list
list1.index("testvalue")  #it will search the list and tell you where is testvalue index
list1.count(10) #how many time 10 is repeated in list, if 10 is in the list it will show how many 10 there are in the list
list1.count("test")  # how many time 10 is repeated in list, if 10 is in the list it will show how many 10 there are in the list
list.sort() #sort all the element
list.reverse() # it will rever all of the list object

## Set function
set(list4) # it will remove the duplicate item
len(set2)
11 in set2 # bring back true or false
11 not in set2
set2.add(16) #add 16 to the set
set2.remove(11) #remove 11 from the set
set1.intersection(set2) #if any item are same it will show it
set1.difference(set2) #all item that  set2 dose not have similar to set1
set1.union(set2) #concat both set and remove the duplicate
set1.pop() #it will remove the first item in set
set1.clear() #clear all item in the set	
