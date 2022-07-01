#learning zip function in python 

list1 = ['India', 'USA', 'Australia', 'UK']
list2 = ['Pune', "New York", "Sydeny", "London"]

s = zip(list1,list2)
print(list(s))

for x,y in zip(list1,list2):
    print(x,y)

#real life examplee
total_cost = [45,67,65,87]
sales_price = [55,77,89,76]

for x,y in zip(total_cost,sales_price):
    print(y-x)