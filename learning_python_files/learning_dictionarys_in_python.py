""" Dictionaries are used to store data in key:value pairs. The are changable (mutable)
Defining Dictionary
Accesing items from dictionary
Adding items to dictionary
Removing items from dictionary"""

demo_dict0 ={}
demo_dict = {1:20, 2:45, 3:50,6:67}
demo_dict1 = {"wa":"testurl","uat":"utaurl"}
demo_dict2 = {"wa":23, 3:"utaurl"}

print(demo_dict0)
print(demo_dict)
print(demo_dict1)
print(demo_dict2)

#you can get the values associated with the kyes in the dictionary. For example you want to get the name of the city 

demo_dict3 = {"city":"Bogota", "country":"Colombia", "population":48000000}

print(demo_dict3["city"]) #It will print Bogota

#To add values to a dictionary you call the dictionary than['key']='value
demo_dict3["colors_of_the_flag"]= "Yellow, Blue, Red"
print(demo_dict3)

#To delete a value from a dictionary you can use the .pop('key') 
demo_dict3.pop('colors_of_the_flag')
print(demo_dict3)

"""Dictionary Methods
get() - retunrs the value for specified key in the dictionary
keys() Returns a copy of the dictionary key's
items() Returns a copy for the dictionary key value pair
values() Returns a copy of the values in the dictionary
pop() removes the dictionary with specifed key
popitem() Removes the arbitrary key:value pair
update() Adds the specifed key-value pair to dictionary
copy() Returns a copy of the dictionary
clear() Removes all the elements from the dictionary"""

demo_dict4 = {"city":"Bogota", "country":"Colombia", "population":48000000}
print(demo_dict4.get("city"))
print(demo_dict4.keys())
print(demo_dict4.items())
print(demo_dict4.values())
print(demo_dict4.pop("population"))
print(demo_dict4.popitem())#removes the last item of the dictionary
print(demo_dict4.update({"flag_color":"Yellow, Blue, Red"}))
print(demo_dict4.copy())
print(demo_dict4.clear())
