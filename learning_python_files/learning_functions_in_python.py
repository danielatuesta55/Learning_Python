#Learning Functions in python 

#Functions are operations that can be re used in other parts of the code just by calling it. 
#define the function and call it 

x = 5 + 9 #this is what we normally do. WE can do this on a function 
print(x)

#key word to define a fucntion is def than you name it how ever you want it like this 
def addition():
    print(12+15) # know you have to call it 

addition()# I dont neet to type print it already does it for you

#normally you would have a varibale for each number like this

x = 5
y = 6

print(x+y)

#here is how to do it in a fnction you just declare them in the function parenthisis

def addition1(x,y): #you declare it here 
    print(x+y) #here you set the addtion funtion
#Now when you call the function you will pass the arguments like this
addition1(15,5) #here the result will be 20
addition1(4,4) #use the function multiple times and just change the values declared 
