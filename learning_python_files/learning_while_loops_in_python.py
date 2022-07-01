#Learning While Loops
"""Used to iterate block of code as long as test expression is true
Test expression is checked first, if expression is evaluated to true body of loop
Conditions are used to stop the loops
Can iterate on list, string, tuples, dictionaries"""




x = 0 
while x <= 10:
    print(x)
    x = x + 1
print("out of while loop")

city = "Melbourne"
#While loops in strings
x = 0
while x < len(city):
    print(city[x])
    x = x + 1 #Always have something like this so you dont get into an infinite loop 

#While loops in lists
cities = ["Bogota", "Chicago", "San Diego", "Madrid"]
x = 0
while x < len(cities):
    print(cities[x])
    x = x + 1 

#While loops in dictionaries
#You cant do while loops in dic here is documentation for loops : https://www.w3schools.com/python/python_dictionaries_loop.asp
demo_dic1 = {"name":"Jorge", "lastname": "Atuesta", "middelname": "Daniel"}

x = 0 
for x in demo_dic1.values():
    print(x)

# While Loops in tuples
countries = ('Colombia','USA',"UK",'Brazil', "Canada", "Argentina", "Spain")

x = 0
while x < len(countries):
    print(countries[x])
    x = x + 1
#______________________________________________________________________
#Break and continue learning python 

#Break: Breaks our form the nearest enclosing loop
#Continue: Go to the start of nearest encolison loop 

#while <expression>
#   <statment(s)> >
#   break 
#   <statment(s)>
#   continue
#   <statment(s)>
#<statement(s)>

#else clause:
#while<expression>:
#   <statment(s)>
#else:
#   <statment(s)>

x = 0
while x <= 1:
    print(x)
    x = x + 1
    break
    print("inside while loop")
print("out side while loop")

x = 0
while x <= 10:
    print(x)
    x = x + 1
    #continue
    print("inside while loop")
print("out side while loop")

x = 0
while x <= 10:
    print(x)
    x = x + 1
    continue
    print("inside while loop")
print("out side while loop")

#else clause

x = 0
while x <= 10:
    print(x)
    x = x + 1
    continue
    print("inside while loop")
else:
    print("out side while loop")

x = 0
while x <= 10:
    print(x)
    x = x + 1
    if x == 5:
        break #This will break and no allow anything else to be printed unlike up top the else clause is ommited and not printe
    print("inside while loop")
else:
    print("out side while loop")