## Tuple
# tuple data can't be changed, but can add new items
pi_tuple = (3,1,4,1,5,9)
new_tuple = list(pi_tuple) #convert tuple to list
new_list = tuple(pi_tuple) #convert list to tuple

my_tuple[0] # will give the first element
my_tuple[-1] # last item
len(pi_tuple)
min(pi_tuple) #smallest item in the tuple
max(pi_tuple)
tuple + (5,6,7) # add these item to tuple
tuple[0:2] #index 0 and 1 will be shown
tuple2[::-1] # show tuple in reverse order
3 in tuple2 #will bring back true or false
del tuple2 #will tottaly delete the tuple

## Tuple packing
tuple1 = ("cisco", "2600", "12.4")
vendor, model, ios = tuple1
print(vendor)
print(model)
print(ios)
