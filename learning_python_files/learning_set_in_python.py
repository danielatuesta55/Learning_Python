#Learning Sets in Python
#Here is the python documentation: https://docs.python.org/3/tutorial/datastructures.html#sets
# sets are () they do not allow duplicate values adn they do not have index for the variables inside 
from code import interact


demo_set_1 = {10,20,30,40}
demo_set_2 = {10.20,'30',40.5}
demo_set_3 = {"10",'30'}

print(demo_set_1)

#say for examle that you have multiple values that are repeted on the set adn you try to print the set it will only use one of those as a unique value
demo_set_4 = {10,10,10,10,10,20,30,40} #multiple 10
print(demo_set_4)#Only prints one 10 

#you can also create a set by calling it instead of using the {}
demo_set_5 = set((45,90,"90","15"))#this will print two 90 since th etype is different one is a string and the other is an integer
print(demo_set_5)

#find the lenght of the set
print(len(demo_set_1))

#check if x value is part of the set
print(20 in demo_set_1) #make sure you are checking in the right type string, float, integer

#______________________________________________________________________________________________________
#Set methods
#documentation source : https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""
len(s)
Return the number of elements in set s (cardinality of s).

x in s
Test x for membership in s.

x not in s
Test x for non-membership in s.

isdisjoint(other)
Return True if the set has no elements in common with other. Sets are disjoint if and only if their intersection is the empty set.

issubset(other)
set <= other
Test whether every element in the set is in other.

set < other
Test whether the set is a proper subset of other, that is, set <= other and set != other.

issuperset(other)
set >= other
Test whether every element in other is in the set.

set > other
Test whether the set is a proper superset of other, that is, set >= other and set != other.

union(*others)
set | other | ...
Return a new set with elements from the set and all others.

intersection(*others)
set & other & ...
Return a new set with elements common to the set and all others.

difference(*others)
set - other - ...
Return a new set with elements in the set that are not in the others.

symmetric_difference(other)
set ^ other
Return a new set with elements in either the set or other but not both.

copy()¶
Return a shallow copy of the set.
"""

demo_set_11= {"Deli","Kolkatea","Melbourne","Sydeny"}
demo_set_12= {"Deli","Kolkatea","Melbourne","Sydeny","Newyork",'Lucknow'}
print(demo_set_11)
#add()
demo_set_11.add("Gold Coast")
print(demo_set_11)
#add()
demo_set_11.remove("Deli")
print(demo_set_11)
#discard()
demo_set_11.discard("Sydeny")
print(demo_set_11)
#pop() - remove any value that is placed at the end at random
demo_set_11.pop()
print(demo_set_11)

#clear() -removes all the elements from the set
demo_set_11_copy = demo_set_11.copy()
print(demo_set_11)
demo_set_11_copy.clear()
print(demo_set_11_copy)

#update()

#joining two sets
#union()
demo_set_11= {"Deli","Kolkatea","Melbourne","Sydeny"}
demo_set_12= {"Deli","Kolkatea","Melbourne","Sydeny","Newyork",'Lucknow'}
#join()
demo_set_13 = demo_set_11.union(demo_set_12)
print(demo_set_13)
#update() you dont need to save it into a variable as it makes the change on it 

#Keep only the duplicate
#intersection()
demo_set_14 = demo_set_11.intersection(demo_set_12)
print(demo_set_14)
#intersection_update()
demo_set_13.intersection_update(demo_set_12)

#symetric()
demo_set_15 = demo_set_11.symmetric_difference(demo_set_12)
print(demo_set_15)
#symetric_difference()
# Keep all excluding the duplicates

#difference() how one set is different than the other if they have the same values than none will appear but if the one you are checking has other values they will appear 
demo_set_16 = demo_set_11.difference(demo_set_12)#none will appear
print(demo_set_16)

demo_set_17 = demo_set_12.difference(demo_set_11)# the ones that are not in demo 11 will appear 
print(demo_set_17)

#you can also use difference_update() as the previous examples it will update the set with no need to store it in a variable

#issubset()
#want to check if subset 1 is sub set 2 
#it returns a boolean yes or no if one is in the other True
z = demo_set_11.issubset(demo_set_12)
print(z)
#issuperset
#Checks to see if it has more values than the other In this case demo set 11 is sub set not super set
#Returns a boolean value
z1 = demo_set_11.issuperset(demo_set_12)
print(z1)
z2 = demo_set_12.issuperset(demo_set_11)
print(z2)