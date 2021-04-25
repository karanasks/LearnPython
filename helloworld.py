# my first python program
# print("Hello World!")

# This is a single line comment

"""Hi
This is a
multiline comment
text
"""

# #number variables
# a=10 #int
# b=1.1 #float
# c=1j #complex
#
# #print type of varable
# print(type(a))
# print(type(b))
# print(type(c))
#
# #int to float
# x = float(a)
# print(x)
#
# #int to complex
# y = complex(a)
# print(y)
#
# #float to complex
# z = complex(b)
# print(z)

"""
Mathematical Operations:
(+)Addition
(-)Subtraction
(*)Multiplication 
(/)Division
(%)Modulus
(**)Exponentiation
(//)Floor division
"""
#
# a = 10
# b = 20
#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b) #a to the power b
# print(a//b)

# print(type(int('12')))

# # Strings
# a='Orange'
# b="""Oranges
# are  always
#    Red
# """
# c = 'Karan from aqua'
# d = '       Karan from London     '
# e = 'Hello, World!'
#
# print(len(a))
# print(b)
# print(len(b))
# print(a[2]) #get char at position 2
# print("from" in c) #check if given string is present
# print(c.upper())
# print(c.lower())
# print(d.strip()) #remove spaces before and after string
# print(a.replace("O", "P"))
# print(c.split("a"))
# print(e[2:5])

# String Methods
# Escape Characters

# # Conditional Statements:
# a = 100
# b = 200
# c = 300
#
# if a > b or a > c:
#     print("a")
# elif a == b and b == c:
#     print("b")
# elif a > b:
#     print("c")
# else:
#     print("d")


# #Functions:
#
# # Create Function:
# def trialFunction():
#     print("Line 1")
#     print("Line 2")
#
# #Call Function:
# trialFunction()
#
# #Function with Parameter:
# def trialFunction2(p1):
#     print(p1 + " World!")
#
# trialFunction2("Hello")
#
# #Function with multiple Parameters:
# def trialFunction3(p1,p2):
#     print(p1 + " " + p2)
#
# trialFunction3("Brown", "Munde!")
#
# for x in range(100):
#     print(x)


mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))