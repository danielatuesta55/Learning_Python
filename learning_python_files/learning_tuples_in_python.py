#Learning Tuples
"""
Tuples are objects that are indexed, they allow duplicated valies and cannot be modified. 
They are inmmutable (no modifications once they are created)

To declare an object as a tuple you will add a varibale than = than () 

They allow mixed values different data types

"""

demo_tuple1 = (1,2,3,4,5)
demo_tuple2 = ("Delhi", "Delhi", "Mumbai", "New York")
demo_tuple3 = (True, False, True, True)
demo_tuple4 = (True, 1, "New York", 23.9)

#you cant modify it after its declare but you can use length function 

print(len(demo_tuple3))
print(type(demo_tuple1))

#Methods of Tuples
#Counting the instances of a value inside the tuple .count()
print(demo_tuple2.count("Delhi"))

#Findign the index of a value inside a tuple
print(demo_tuple2.index("Delhi"))

#accesing the value wiht indiex
print(demo_tuple2[3])

for x in demo_tuple2:
    print(x)

#join tuples
joined_tuple = demo_tuple1+demo_tuple2+demo_tuple4
print(joined_tuple)
#checked type
print(type(joined_tuple))
#print cerain values from specific index 
print(joined_tuple[0:3])