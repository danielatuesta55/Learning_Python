#if you have questions reference this video https://youtu.be/epZx21uanRI?list=PLL34mf651faPOf5PE5YjYgTRITzVzzvMz
#String functions in Python 
""" Here is a short list of some string functions available in Python
1. len(s) : Return the number of items in an object
2. srt() : Converts specified value into a String
3. upper() : Converts a String into upper case for upper you have to do the variable than .upper()
4. lower () : Converts a String into lower case
5. count (ub[,end]])) : Returns the number of times a specified value is foind in the String
6. isupper() : Returns True if all character in the string are upper case
7. islower() : Returns True if all characters in the String are lowe case
8. split(sep=None, maxsplit=-1): Splits the string at the specifed separator, adn retunrs 
9. rsplit: Splits a string into a list, starting from the right
10. strip(): Returns a trimmed version of the string
11. replace(old, new[, count]): Replaces the string fro a specified phrase with another specified phrase
12. find(sub[,start[,end]]): Searches the string for a specified value and retunrs the 
13. index(sub[,start[,end]]): Searches the string for a specific 

"""
# If you want to learn more and therte are many more you can always look at the documentation search for string operations click on it and at the top click on the string methods and you will have the whole python documentation
#1. len(s) : Return the number of items in an object
from functools import update_wrapper
from turtle import st


x = "This is a string"
print(len(x)) # It counts blank space 

# 2. srt() : Converts specified value into a String
y = 1654321
z= str(y)
print(type(z))
# 3. upper() : Converts a String into upper case
xx = (x.upper())
print(xx)
# 4. lower () : Converts a String into lower case
print(xx.lower())
# 5. count (ub[,end]])) : Returns the number of times a specified value is foind in the String
x = "This is a very long string that makes no sense and I created it to test the string funcion count. is is is is is "
print(x.count("is")) #counting the number of times is present in the string
#you can have a start and end if you want for example I am going to start to count after index 10 
print(x.count("is", 10, ))

# 6. isupper() : Returns True if all character in the string are upper case
# 7. islower() : Returns True if all characters in the String are lowe case
# 8. split(sep=None, maxsplit=-1): Splits the string at the specifed separator, adn retunrs 
# 9. rsplit: Splits a string into a list, starting from the right
# 10. strip(): Returns a trimmed version of the string
# 11. replace(old, new[, count]): Replaces the string fro a specified phrase with another specified phrase
# 12. find(sub[,start[,end]]): Searches the string for a specified value and retunrs the 
# 13. index(sub[,start[,end]]): Searches the string for a specific 
