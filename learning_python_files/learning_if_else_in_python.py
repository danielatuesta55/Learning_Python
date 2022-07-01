#Learning IF ELSE statments in python 
# IF ELSE are statments that give you consequences based on a decision 
# IF I score x in the test I get an A+ else D

#score = print(input("What is your test score:"))
score = 94
if score >90:
    print("I get motorbike")
else:
    print("You dont get anything")

#using elif is an option to add other consequences to the decision 
score = 55
if score >90:
    print("I get motorbike")
elif score >75 and score <90: #you can have as many as you like
    print("You get ice cream")
elif score >40 and score < 75:
    print("You get a lego")

else:
    print("You dont get anything")