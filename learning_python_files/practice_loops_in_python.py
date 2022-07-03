#This file has been made so I can practice my loops and methods. I was sitting in by the pool and had to come up and try some of this out
#Started by creating all types of objects. You can double check with the printed messade of type()
from hashlib import new


string1 = "Jorge"
#print(type(string1))

string2  = "Daniel"
#print(type(string2))

list1 = ['iPad','iPhone','macbook','screen','bottel cap','paper','keyboard', 'mouse','bat']
#print(type(list1))

list2 = ['couch','tv','remote control', 'play station', 'chair', 'blanket', 'table', 'mug']
#print(type(list2))

tuple1 = (1,2,3,4,5,6,7,8,9)
#print(type(tuple1))

tuple2 = (83.0,82.5,81.5,81.5,82.8)
#print(type(tuple2))

dict1 = {"country":"Colombia","city":"Bogota","country":"USA","city":"Chicago","country":"USA","Spain":"Madrid"}
#print(type(dict1))

dict2 = {"male":80,'female':68,"male":86,'female':88,"male":100,'female':75}
#print(type(dict2))

set1 = {'cool','bannanas', 'life','podcast','enjoy','coding'}
#print(type(set1))

set2 = {85,63.2,65,98,84,110,5,55,5.5}
#print(type(set2))


#Practicing for loops from string to list 
listfromstring = []
for letter in string1:
    listfromstring.append(letter)
print("A new list was created from the string thanks to the while loop")
print(listfromstring)

#practicing for loops from list to list only if it starts with letter i 

items_with_letter_i = []

for item in list1:
    if item[0]=="i":
        items_with_letter_i.append(item)
    else: 
        pass
print(items_with_letter_i)

#practicing for loops from list to list only if it does not starts with letter i 

items_do_not_start_with_letter_i = []

for item in list1:
    if item[0]!="i":
        items_do_not_start_with_letter_i.append(item)
    else: 
        pass
print(items_do_not_start_with_letter_i)

#Nested loop to iterrate through two lists and append to a new list 

new_list_all_items = []

for item in list1:
    new_list_all_items.append(item)
    for item in list2:
        new_list_all_items.append(item)
print("Here is your new list: {}".format(new_list_all_items))

#loop to iterrate through two list but only append words starting with letter b
list1 = ['iPad','iPhone','macbook','screen','bottel cap','paper','keyboard', 'mouse','bat','Baseball']

list2 = ['couch','tv','remote control', 'play station', 'chair', 'blanket', 'table', 'mug']

list_letter_b = []

for item in list1:
    if item[0] == "b":
        list_letter_b.append(item)
for item in list2:
    if item[0] == "b":
        list_letter_b.append(item)
print("Here is your new list with only items starting with letter b or B {} ".format(list_letter_b))
