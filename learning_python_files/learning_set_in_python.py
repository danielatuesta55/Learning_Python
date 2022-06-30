#Learning Sets in Python
#Here is the python documentation: https://docs.python.org/3/tutorial/datastructures.html#sets
# sets are () they do not allow duplicate values adn they do not have index for the variables inside 
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
