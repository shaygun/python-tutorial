# Loop

## For Loop  Example 1
the_count = [1, 2, 3, 4, 5]
for number in the_count:
    print "This is count %d" % number

## For Loop Example 2
elements = []
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)

## For Loop Example 3
for x in range(0,10): #for lopp until 9 not 10
    print(x, '', end="")

grocery_list= ['juice', 'tomatoes', 'potatoes', 'bananas']
for y in grocery_list:
    print(y)

for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])

for element in range (len(vendors)):
    print vendors[element_index] #will print all element

for element in vendors:
    print element
else:
    print "this is the end of loop"

for i in range():
    pass # it will just do nothing, it will allow to keep the for loop there only, for loop dosnt do anything

##############################################################################
# converting complex tuple to dictionary
test1 = [
        ('ge-0/0/1.0', [('interface', u'ge-0/0/1.0'), ('ip', u'1.1.1.1'), ('mac', u'00:0c:29:f4:a4:9a'), ('age', 1247.0)]),
        ('ge-0/0/0.0', [('interface', u'ge-0/0/0.0'), ('ip', u'10.10.10.1'),('mac', u'00:0c:29:b2:ce:09'), ('age', 1407.0)]),
        ('em0.0', [('interface', u'em0.0'), ('ip', u'128.0.0.16'), ('mac', u'fe:00:00:00:00:04'), ('age', 632.0)]),
        ('em1.32768', [('interface', u'em1.32768'),('ip', u'192.168.1.1'), ('mac', u'aa:bb:cc:dd:ee:ff'), ('age', 1255.0)])
        ]

arp_table = []
for arp_table_entry in test1:
    arp_entry = {
        elem[0]: elem[1] for elem in arp_table_entry[1]
        }
    arp_table.append(arp_entry)

# result
test2 = [
        {'interface': u'ge-0/0/1.0', 'ip': u'1.1.1.1', 'mac': u'00:0C:29:F4:A4:9A', 'age': 1247.0},
        {'interface': u'ge-0/0/0.0', 'ip': u'10.10.10.1', 'mac': u'00:0C:29:B2:CE:09', 'age': 1407.0},
        {'interface': u'em0.0', 'ip': u'128.0.0.16', 'mac': u'FE:00:00:00:00:04', 'age': 632.0},
        {'interface': u'em1.32768', 'ip': u'192.168.1.1', 'mac': u'AA:BB:CC:DD:EE:FF', 'age': 1255.0}
        ]
print (test2[0]['mac'])
#############################################################################
