## Dictionaries
## they index by key
## each key should be unique
## Example 1
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
cities['NY'] = 'New York' #add some more cities
print "NY State has: ", cities['NY']
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city " % (state, abbrev)

## Example 2
super_villains = {'fiddler': 'Isaac bowih', 'Captain Cold': 'Leonard snart', 'weather wizard': 'mark mardon'}
print(super_villains['Captain Cold'])
del super_villains['fiddler']
super_villains['leonard snart'] = 'hartley rathway'
print(len(super_villains))
print(super_villains.get("leonard snart"))
print(super_villains.keys()) #print only the keys which is the first part
print(super_villains.values()) #print the second part of dictionary
print(super_villains.items()) #it will show key and item in seperate tuple value
