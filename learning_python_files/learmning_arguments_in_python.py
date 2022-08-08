# Learning Arguments in Python 

#Positional Arguments
#Keyword arguments
#Requiered Arguments
#Optinal Arguments

def sub_demo(x,y): #This are the required arguments
    return x - y #This are parameters

z = sub_demo(8,4) #This are arguments

print(z)

#positional arguments are the way that the values are being placed in the arguments that have a connection to the parameters
#In this case we see the positional arguments for  8 and 4 are x and y 
#you can not call a function without the requiered arguments as it will give a required arguments error
#Optionala rguments means that you do not have to declare them in the arguments because they have an initial value
#When the function is called here is an example

def sub_demo(x=5,y=10): #This are the required arguments
    return x - y #This are parameters

ty = sub_demo() #This are arguments

print(ty)
