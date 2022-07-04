#Learning Break and Continue in While loops
"""break: Breaks out from the nearest enclosing loop
continue: Go to the start of neaest enclosing loop

while <expression>:
    <statements>
    break
    <statment>
    continue
    <statments>
<statment>

else clause:
while <expression>:
    <statemnets>
else:
    <statements>"""

from traceback import print_tb


x = 0 
while x <= 10:
    print(x)
    x = x + 1
    break #Just prints 0 and comes out of the loop it stops the loop if condition keppes going.
print("out of while loop")
#continue
x = 0 
while x <= 10:
    print(x)
    x = x + 1
    continue
    print("inside while loop") #it will not allow the print statment to print inside the loop and it just goes up to and continues the loop
print("out of while loop")
#break
x = 0
y = 0  
while x <= 10:
    print(x)
    x = x + 1
    print('inside the parent while loop')
    while y <= 5:
        print(y)
        break #breaks out of this inner loop but allows the parent loop to continue to work
        print('inner loop')
print('outside of while loop')
#continue
x = 0
y = 0  
while x <= 10:
    print(x)
    x = x + 1
    print('inside the parent while loop')
    while y <= 5:
        print(y)
        y = y + 1
        continue #will allow the child loop to cycle first and then go to the parent loop
        print('child loop')
print('outside of while loop')

#no break or contiune
x = 0
y = 0  
while x <= 10:
    print(x)
    x = x + 1
    print('inside the parent while loop')
    while y <= 5:
        print(y)
        y = y + 1
        #will allow the child loop to cycle first and then go to the parent loop
        print('child loop')
print('outside of while loop')

#else clause

#no break or contiune
x = 0
while x <= 10:
    print(x)
    x = x + 1
    print('parent loop')
else:
    print('outside of while loop') #This will get executed

    #else clause

#break- it will break and it will not print out the else statment 
x = 0
while x <= 10:
    print(x)
    x = x + 1
    if x == 5:
        break
else:
    print('outside of while loop')#does not get printed as the loop got break clause