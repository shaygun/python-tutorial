## Class
## A class is a way to take a grouping of functions and data and place them inside a
## container so you can access them with the '.' (dot) operator.

## Example 1
class Point(object):
    @staticmethod # use static whenever we dont use dynamic self and __init__ to initialize variable
    def distance():
        x = 6
        y = 8
        """Find distance from origin"""
        return (x**2 + y**2) ** 0.5
a = Point()
print(a.distance())

## Example 2
class Point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x # self.x and x is tottaly different, self.x is only accessible from class
        self.y = y

    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5

    def distance2(self, something):
        """Find distance from origin"""
        return (self.x**2 + self.y**2 + something**2) ** 0.5

a = Point(6, 8)
print(a.distance())
print(a.distance2(44))

## Example 3 (Inheritance)
class parent(object):
    def implicit(self):
        print "PARENT IMPLICIT()"
class child(parent):
    pass # do nothing, when your function or class is empty you will need it
dad = parent()
son = child()
dad.implicit()
son.implicit()

## Example 4 (Inheritance - override)
## You can simply override parent function in child class
class parent(object):
    def override(self):
        print "PARENT IMPLICIT()"
class child(parent):
    def override(self):
        print "Child override()"
dad = parent()
son = child()
dad.override()
son.override()

## Example 4 (Inheritance - Altered)
## this is usefull when you want to make a change to parent function but
## you dont want to rewrite the whole function and still want to execute the
## parent function too
class parent(object):
    def altered(self):
        print "PARENT Altered()"
class child(parent):
    def altered(self):
        print "Child Before PARENT Altered()"
        super(child, self).altered()
        print "Child, AFTER PARENT ALTERED()"
dad = parent()
son = child()
dad.altered()
son.altered()

## Example 5 (Composition)
## same example as above but using composition, It just make a object out of parent class
class parent(object):
    def override(self):
        print "parent override()"
    def inherit(self):
        print "parent inherit()"
    def altered(self):
        print "parent alterd()"

class child(object):
    def __init__(self):
        self.parent = parent()
    def inherit(self):
        self.parent.inherit()
    def override(self):
        print "CHILD Override()"
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.parent.altered()
        print "CHILD, AFTER OTHER altered()"
son = child()
son.inherit()
son.override()
son.altered()
