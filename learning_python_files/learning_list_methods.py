"""Learning list methods in python
1. list.append(x)
2.list.insert(1,x)
3.list.remove(x)
4.list.pop([i])
5. list.index(x[, start[,end]])
6.list.count(x)
7.list.sort(",key=none, reverese=false)
8. list.reverse()
9. list.copy()
10. list.clear()
"""
#Here is the python documentation doc where you can find all of this list methods- https://docs.python.org/3/tutorial/datastructures.html

cities = ["Bogota","Deli","Mumbai","Melbourne","Sydney", "Kolkata"]

# 1. list.append(x)
cities.append("Chicago")
print(cities)
# 2.list.insert(x)
cities.insert(1,"Madrid") #1 is the index where Madrid is going to go in this case #2 in the list
print(cities)
# 3.list.remove(x)
cities.remove("Chicago")
print(cities)
# 4.list.pop([i])
cities.pop(1)
print(cities)
# 5. list.index(x[, start[,end]])
print(cities.index("Bogota"))
# 6.list.count(x)
print(cities.count("Sydney"))
# 7.list.sort(",key=none, reverese=false)
cities.sort()
print(cities)#if you leave it empty it will sort it alphabetically
# 8. list.reverse()
cities.reverse()
print(cities)
# 9. list.copy()
new_cities = cities.copy()
print(new_cities)
# 10. list.clear()
new_cities.clear()
print(new_cities)