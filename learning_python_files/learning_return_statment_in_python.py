#Learning the return function on python
#first define a function 

def addition1(x,y): #you declare it here 
    print(x+y) #here you set the addtion funtion

#instead of using the print function you should use return. This will return the process result to be used in any other part of your program
def addition2(x,y): #you declare it here 
    return x+y #here you use return statement so the code knows what to do
#you can know store the value of the functions return in a variable like this:
z = addition2(100,5)
print(z)

#It is super important to note that the number of arguments set on the function need to be passed on the calculation for it to work. In our addition sample we had two (x,y) and this are the numbers we added
#you can create a doc string for people reading your code to understadn the function and why it was created you do it by adding """ and enter it will auto populate.
def addtion3(x,y,a):
    """
    x:
    y:
    a:
    return: 
    """
    return x+y+a
z = addition3(1,100,5)
print(z)