#Learning for loops in python
#used to iterate over the sequence like list, string, dic, set or tuple
#Less like the for loop in other programming languanges

from itertools import count


city = ["Delhi","Mealbourne","Lucknow","Sydney"] #same for string tuples adn sets

for c in city:
    print(c)


cities = [["India","Delhi"],["Sydney","Mealbourne"],["Canada","Lucknow"],["USA","New York"]] 

for country, city in cities:
    print("country is "+ country,"and city is "+ city)

#For dictionarys
#function to convert into dictionary 
my_dic = dict(cities)
print(my_dic)
#for loop in dic 
for country, city in my_dic.items(): #Make sure you use the .item() method for dictionary or else it will not allow you to loop through
    print(country, city)

#nested loops
my_dic = dict(cities)
print(my_dic)
#for loop in dic 
for country, city in my_dic.items(): #Make sure you use the .item() method for dictionary or else it will not allow you to loop through
    print(country, city)
    for s in country: #nested for loop to print character
        print(s)# Prints the country and the city and than each character of the country 