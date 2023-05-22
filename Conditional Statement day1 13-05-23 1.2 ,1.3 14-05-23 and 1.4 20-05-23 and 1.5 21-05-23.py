#!/usr/bin/env python
# coding: utf-8

# # IF
# # ELIF
# # Else
# #### 13May2023

# # Indentation apply on  
# * Identation means just like fix space and which space comes after enter ":"---like 
# if x%2==0:
#    print(x,"Even Number")
# * Conditional Statements
# * Loop
# * Function

# * if condition1 and condition2:
# * -----statements/Action/prints
# * elif condition2 :
# * -----statements/Action/Prints
# * elif condition3 : 
# * -----statements/Action/Prints
# * else:
# * -----statements/Action/Prints
#      

# In[8]:


x=-2
if x>10:
    print(x,"is greater then 10")
else:
    print(x,"is not greater than 10")


# In[9]:


#2 Print whether given number is + or - or 0


x=-45
if x>0:
    print(x,"is Positive")
elif x<0:
    print(x,"is not neagtive")
else:
    print("Zero")


# In[ ]:


# "="----value assign


# In[10]:


# "=="------compare value
# "f"--------format


# In[12]:


#3 Check whether given number is even or not ?

x=4
if x%2==0:
    print(f"given number {x} is even number")
else:
    print(f"given number {x} is not a even number")


# # INPUT

# In[13]:


n=input("Enter your number")


# In[17]:


x=int(input("Enter your Number"))
if x>10:
    print(x," is greater than 10")
else:
    print(x,"is not grater than 10")


# In[43]:


x=int(input("Enter your number :"))
if x%2==0:
    print(f"{x} is Even number")
else:
    print(f"{x} is not even number")


# In[24]:


# check create a program to check for voting elei
x=int(input("Enter your Age"))
if x>=18:
    print(x,"Age are eligible for voting")
else:
    print(x,"Age Not Eligible fro voting")


# In[41]:


#1 wap to return last digit of a given number
x=int(input("Enter number"))
if a=x%10:
    print(x,"Last digit number is",a) 
    


# In[42]:


#2 wap to check that last digit of a number is divisible by 3
x=int(input("Enter the number"))
if x%10%3==0:
    print(f"last digit of given number {x} is {x%10} which is divisible by 3")
else:
    print(f"last digit of given number {x} is {x%10} which is not divisible by 3")


# In[ ]:


#3 wap to find the smallest number of two numbers
x=int(input('Enter a X number'))
y=int(input('Enter a Y number'))
if x>y:
    print(f"")


# In[ ]:


#4 wap to find largest no. of two numbers


# In[37]:


#5 wap to check the divisibility by 2 & 3 both-----(if x%2==0 and x%3==0)
a=int(input("Enter a number"))
if a//2=!0 and a//3=!0:
    print('true1')
else:
    print("false2")


# # LOOPS-----------1.3
# #### 14May2023

# In[46]:


ls=[19,34,54,58,11]
if ls[2]%2==0:
    print("This is even number")
else:
    print("This is not even number")


# <!-- for and while loop
# * For loop :- It is a finite loop()
# * While Loop :- It is Infinite Loop()       -->

# For and While loop
# * Loop :- It is finite loop
# * While loop:- It is Infinite loop
# * Iterator Like (i) ----

# ## For i in object:
# ##    action/statement/return/print

# In[55]:


ls=['Harry','john','Dawn','jimmy','zhuhao','Yu','mariat','Jennet','Kang','Tony','Steve','star']

for i in ls:
    print('Good Morning !' ,i, 'Welcome to Disny World')
##    print(f"Good Morning,{i}")
    


# In[58]:


numls=[2,4,19,2,14,10,31,5,3,44]
for i in numls:
    print(i," Square root is" ,i**2)


# In[59]:


txt0='Python'
for i in txt0:
    print(i)


# In[65]:


numls


# In[66]:


for i in numls:
    if i>=20:
        print(i)


# In[70]:


for i in numls:
    print("Greater than 20 is :",(i>=20)!=0,", e.g.: ",numls[])


# In[73]:


# Create a program to print the table of a given number
## x=int(input("Enter a number"))
for i in range(1,11):       # Start is including and last /end number is not including
    print(i)
    


# In[74]:


for i in range(1,11,3):       # Start is including and last /end number is not including and here '3' role is jump the 3 step 
    print(i)


# In[78]:


x=int(input("Enter a number"))
for i in range(1,11):       # Start is including and last /end number is not including
    print('Table of :',x,"is",x,"*",i,"=",x*i)


# In[82]:


x=int(input("Enter a number "))
for i in range(1,11):
    print(f'{x}*{i} = {x*i}')


# In[ ]:


# WAP to print first 10 natuaral numbers and its square


# In[81]:


for i in range(1,11):
    print(i," is natural number and there square is" ,i**2)


# In[85]:


#1 WAP to print 'n' natural number in reversival order
n=10
for i in range(0,n):
    print(n-i)


# In[86]:


#1 WAP to print 'n' natural number in reversival order
n=5
for i in range(n,0,-1):
    print(i)      # another method
    


# In[ ]:


#2 WAP to get the sum of first N natural number
#3 WAP to print the even number b/w two number entered by users 
#4 WAP to count the odd number b/w two numbers entered by users
#5 WAP to find the factors of a number


# In[88]:


#2 WAP to get the sum of first N natural number
n=int(input("Enter the number "))
x=0
for i in range(1,n+1):
    x=x+i
    print(f"sum of first {n} natural number is {x}")


# In[90]:


#3 WAP to print the even number b/w two number entered by users
n=int(input("Enter a number"))
final_sum=n*(n+1)/2
print(f"Sum of first {n} natural number is {final_sum}")


# In[94]:


#4 WAP to count the odd number b/w two numbers entered by users
x=int(input("Enter 1st number :"))
y=int(input("Enter 2nd number :"))
for i in range(x,y+1):
    if(i%2==0):
        print(i)     


# In[105]:


#5 WAP to find and save the factors of a number
n=10
fact=[] # fact=list()
for i in range(1,n+1):
    if n%i==0:
        fact.append(i)
    print(f"factors of {n} are \n {fact}")


# In[101]:


# wap to count the count the odd number b/w two numbers entered by user
x=int(input("Enter 1st number :"))
y=int(input("Enter 2nd number :"))
count=0
for k in range(x,y+1):
    if k%2!=0:
        count=count+1
print(f"Total number of odd b/w {x} and {y} are {count}")        


# In[ ]:


# wap to print the following pattern ## Half Parameter
A)
1
1 2
1 2 3
1 2 3 4

B)
****
***
**
*


# In[227]:


for i in range(1,6):
    for k in range(1,i-0):
        print(k,end=" ")
    print()


# In[114]:


for i in range(1,6+1):
    for k in range(1,i+1):
        print(k,end=" ")
    print()


# In[115]:


for i in range(1,6+1):
    for k in range(1,i+1):
        print(k,end=" ")
    print("\n")


# In[119]:


for i in range(1,6+1):
    for k in range(1,(i+1)):
        print("*",end=" ")
    print(" ")


# In[ ]:


1
2 2
3 3 3
4 4 4 4
5 5 5 5 5


# In[123]:


for i in range(1,6+1):
    for k in range(1,(i+1)):
        print(i,end=" ")
    print(" ")


# In[133]:


# Inverted half pyramid
55555
4444
333
22
1




for i in range(6,0,-1):
    for k in range(1,(i+1)):
        print(i,end=" ")
    print(" ")


# In[ ]:


# Pattern
1
2 1 
3 2 1
4 3 2 1
5 4 3 2 1
6 5 4 3 2 1


# In[153]:


for i in range(1,6+1):
    for k in range(i,0,-1):
        print(k,end=" ")
    print(" ")


# In[ ]:


#         1 
        1 2
      1 2 3
    1 2 3 4
  1 2 3 4 5
1 2 3 4 5 6


# In[160]:


for i in range(1,6+1):
    for k in range(1,6-i+1):
        print(" ",end="")
    for l in range(1,i+1):
        print(l,end="")
    print()    


# In[161]:


for i in range(1,6+1):
    for k in range(1,6-i+1):
        print(" ",end="")
    for l in range(1,i+1):
        print(l,end=" ")
    print()   


# In[163]:


for i in range(1,6+1):
    for k in range(1,6-i+1):
        print(" ",end="")
    for l in range(1,i+1):
        print(chr(l+64),end=" ")
    print()


# In[167]:


for i in range(1,6+1):
    for k in range(1,6-i+1):
        print(" ",end="")
    for l in range(1,i+1):
        print(chr(l),end=" ")
    print()


# In[ ]:


#
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21


# In[184]:


d=1
df=1
for i in range(1,10):
    for k in range(i,i+d):
        print(df,end=" ")
        df+=1
    print()
    d+=1


# In[209]:


*Task
*Given an integer, , perform the following conditional actions:

*If  is odd, print Weird
*If  is even and in the inclusive range of 2 to 5 , print Not Weird
*If  is even and in the inclusive range of  6 to 20 , print Weird
*If  is even and greater than 20,print Not Weird



x=intput(int("Enter the eneter"))
if x%2!=0 and (6>=x<=20) :
    print("Weird") 
elif (2>=x<=5) :
    print("Not Weird")
elif (x>20) :
    print("Not Weird")
else:
    print("the data")    
              
            


# In[199]:



 
#elif (2>=x<=5):
 #   print("Not Weird")
#elif (6>=x<=20):
#    print('Weird')
#elif (x>20):
 #   print("Not Weird")
#else:
 #   print("the data")    
            


# In[222]:


x=10
if any([6>=x<=20 and x%2!=0]):
    print("weird")
elif any([2>=x<=5 and x>20]):
    print("Not Weird")
else:
    print("No idea")


# In[225]:


*Task
*Given an integer, , perform the following conditional actions:

*If  is odd, print Weird
*If  is even and in the inclusive range of 2 to 5 , print Not Weird
*If  is even and in the inclusive range of  6 to 20 , print Weird
*If  is even and greater than 20,print Not Weird






n = int(input("Enter an integer: "))

if n % 2 != 0:
    print("Weird")
else:
    if n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
        
        
--------------------------------------------------------------
n = int(input("Enter an integer: "))

if n % 2 != 0:
    print("Weird")
elif n%2==0 and n in range(2,6):
    print("Not Weired")
elif n%2==0 and n in range(6,21):
    print("Weired")
elif n%2==0 and n>20:
    print("Not Weired")


# # H.C.F. / GCD
# ##### 20May2023

# * 1. CAP to find the gcd/hcf of two numbers

# In[235]:


n1=int(input("Enter the N1 number :"))
n2=int(input("Enter the N2 number :"))
fact_n1=[]
for i in range(1,n1+1):
    if n1%i==0:
        fact_n1.append(i)

fact_n2=[]        
for j in range(1,n2+1):
    if n2%j==0:
        fact_n2.append(j)
        
com_fact=[]
for k in fact_n1:
    if k in fact_n2:
        com_fact.append(k)
print("GCD : ",max(com_fact))        
        
        


# * 2. CAP to check the prime number

# In[242]:


## 2 and greater than 2
n=2
fact_n=[]
for a in range (2,n):
    if n%a==0:
        print("Not a prime")
        break
        
else:
    print("Prime")


# In[248]:


n=13
if n==1:
    print("Not a prime")
else:
    for i in range (2,n):
        if n%i==0:
            print("Not a prime")
            break
else:
    print("Prime")


# * 3. Find the  prime number b/w two numbers?

# In[262]:


n=100
n1=500
gh=[]
for k in range (2,20):
    for i in range(2,k):
        if k%i==0:
            break
    else:
        gh.append(k)
gh


# * 4. Find the factorial of given number
# * 4!=4*3*2*1
# * 10!=10*9*8*7*6*5*4*3*2*1

# In[265]:


n=5
m=1
for i in range(1,n+1):
    m=m*i
print(m)    


# * 5. Fibonocci Series

# In[ ]:


1,1,2,3,5,8,13,21,.........


# In[266]:


a=1
x=i
x=[]
for i range(1,1*x):
    x=x*i+a*1
print(x)    


# # While LOOP 
# #### 20may2023

# In[270]:


n=2000
t=2000
t=.15/12
cnt=0
while n<=10000000:
    n=n*(1+t)+k
    # print(n)
    cnt+=1
print(cnt/12)    
    


# * 6. Find the factorial of given number

# In[272]:


n=5  ## find Factorial number
k=1
while n>0:
    k*=(n)
    n=n-1
print(k)    


# # Function in PYTHON

# * Build in Functions :- Sum,fro,len,set,dict,tuple.......etc
# * User Defined function :- Functions which user creates for its usages
# * Annonymous Function :- Lambda function (One line function)     

# In[ ]:


# # Syntax for user defined function
# def function_name(arg1,arg2,arg3,arg4.......):                ## arg-values
#     """ docstring : about the functions and its usages
#     edfg
#     erfgh
#     efhjf
#     """
#     action/statement/condition/etc........
#     print()/return


# In[278]:


import random as rm
rm.choices([2,5,323,24,1,45,23],k=2)


# In[279]:


def mysum_two_number(x,y):
    """This program is created for getting the sum of two numbers x and y
    details:
    x: any number
    y: any number
    
    examples:
    x=2 ; y=4
    z=x+y
    ==> 6
    """
    z=x+y
    print(z)


# In[280]:


mysum_two_number(1,3)


# In[281]:


# Create a function to get square root of a number?
z=(x)**(1/2)

def sqroot(x):
    z=(x)**(1/2)
    return z


# In[282]:


sqroot(4)


# In[284]:


sqroot(8)


# In[285]:


#  create a function to get N th root of a number
# z=(x)**(1/n)
def root(x,n):
    z=(x)**(1/n)
    return z


# In[287]:


root(5,2)


# In[298]:


## use +,-,* operators at one time
a = int(input())
b = int(input())
print(a+b) 
print(a-b)  
print(a*b)


# ## Task
# The provided code stub reads two integers, a and b , from STDIN.
# 
# Add logic to print two lines. The first line should contain the result of integer division,  a//b . 
# The second line should contain the result of float division, a /b .
# 
# No rounding or formatting is necessary.
# 
# Example
# a=3
# b=5
# 
# 
# The result of the integer division 3//5=0.
# The result of the float division is 3/5=0.6.

# In[300]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a//b))
    print(float(a/b))


# ## Area of Circle          1.5
# 
# ### 21May2023

# In[306]:


# a=pi * (r**2)            
def area_circle(pi=22/7,r):      ## Here non default argument follows default argumenet
    a=pi*(r**2)
    return a


# In[308]:


def area_circle(r,pi=22/7):
    a=pi*(r**2)
    return a


# In[309]:


area_circle(5)


# #### Key Argumenent Usage

# In[312]:


area_circle(r=5,pi=3.14)


# #### Positional arguments Usages

# In[313]:


area_circle(3.14,5)


# #### Annonymous Arguments

# In[315]:


def mysumfunction(*args):              ##### Sum=0,multiple=1
    s=0
    for i in args:
        s+=i
    return s    
        


# In[316]:


mysumfunction(2,4,6,3,4,6,4,3,6,8,9)


# In[317]:


def myproductfunction(*args):              ##### Sum=0,multiple=1
    s=1
    for i in args:
        s*=i
    return s    
        


# In[318]:


myproductfunction(3,5,3)


# In[321]:


def mykey(*kwargs):
    for key, value in kwargs.items():
        print(value*2)


# In[325]:


mykey(4)


# ### Scope in Python
# * Local Variable
# * Global Variable

# In[326]:


def cylinder(r,h):
    TSA=2*pi*r*(r+h)
    SA=2*pi*r*h
    vol=pi*(r**2)*h
    d={"Total surface area" : TSA,
    'Surface area' : SA,
    'Volume' : vol}
    return d


# In[327]:


cylinder(10,11)


# In[328]:


pi=22/7
cylinder(2,4)


# In[329]:


cylinder(r=10,h=23)


# ### Annonymous Functions
# * They dont have actually any name. Can be stored in any variable
# * Multiple inputs are there but single output
# * One Liner

# # Lambda
# ### x=lambda a:actions on a 

# In[332]:


# Q1: Create a program to calculate square of a number
def mysqr(a):
    z=(a)**2
    return z


# In[333]:


mysqr(2)


# In[338]:


abc=lambda a :(a)**2


# In[339]:


abc(2)


# In[347]:


#2 Nth root
## z=(x)**(1/n)
abd=lambda x,n :(x)**(1/n)


# In[348]:


abd(10,3)


# In[353]:


#3 Minimum number of two
xyz=lambda  a,b: print(a ,"is less than", b) if a>b else y


# In[354]:


xyz(2,4)


# In[365]:


a=[2,4,10,3,5,11,35]
# make square of all the numbers and save them into a list

# numls=[2,4,19,2,14,10,31,5,3,44]
# for i in numls:
#     print(i," Square root is" ,i**2)


# In[379]:


list(map(lambda i: i**2,a))                 ##### Map use for multiple loop apply


# In[380]:


list(map(lambda i:str(i),a))


# ## Filter

# In[403]:


# Q-Filter out the numbers which are greater than 10 and save them into list
a=[2,4,10,3,5,11,35]


# In[404]:


b=[]
for k in a :
    if k>10:
        b.append(k)


# In[405]:


b


# In[406]:


list(filter(lambda x:x>10,a))


# In[407]:


# Python Program to Print Hello world!
# Python Program to Add Two Numbers
# Python Program to Find the Square Root
# Python Program to Calculate the Area of a Triangle
# Python Program to Solve Quadratic Equation
# Python Program to Swap Two Variables
# Python Program to Generate a Random Number
# Python Program to Convert Kilometers to Miles
# Python Program to Convert Celsius To Fahrenheit
# Python Program to Check if a Number is Positive, Negative or 0
# Python Program to Check if a Number is Odd or Even
# Python Program to Check Leap Year
# Python Program to Find the Largest Among Three Numbers
# Python Program to Check Prime Number
# Python Program to Print all Prime Numbers in an Interval
# Python Program to Find the Factorial of a Number
# Python Program to Display the multiplication Table
# Python Program to Print the Fibonacci sequence
# Python Program to Check Armstrong Number
# Python Program to Find Armstrong Number in an Interval
# Python Program to Find the Sum of Natural Numbers
# Python Program to Display Powers of 2 Using Anonymous Function
# Python Program to Find Numbers Divisible by Another Number
# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
# Python Program to Find ASCII Value of Character
# Python Program to Find HCF or GCD
# Python Program to Find LCM
# Python Program to Find the Factors of a Number
# Python Program to Make a Simple Calculator
# Python Program to Shuffle Deck of Cards
# Python Program to Display Calendar
# Python Program to Display Fibonacci Sequence Using Recursion
# Python Program to Find Sum of Natural Numbers Using Recursion
# Python Program to Find Factorial of Number Using Recursion
# Python Program to Convert Decimal to Binary Using Recursion
# Python Program to Add Two Matrices
# Python Program to Transpose a Matrix
# Python Program to Multiply Two Matrices
# Python Program to Check Whether a String is Palindrome or Not
# Python Program to Remove Punctuations From a String
# Python Program to Sort Words in Alphabetic Order
# Python Program to Illustrate Different Set Operations
# Python Program to Count the Number of Each Vowel
# Python Program to Merge Mails
# Python Program to Find the Size (Resolution) of a Image
# Python Program to Find Hash of File
# Python Program to Create Pyramid Patterns
# Python Program to Merge Two Dictionaries
# Python Program to Safely Create a Nested Directory
# Python Program to Access Index of a List Using for Loop
# Python Program to Flatten a Nested List
# Python Program to Slice Lists
# Python Program to Iterate Over Dictionaries Using for Loop
# Python Program to Sort a Dictionary by Value
# Python Program to Check If a List is Empty
# Python Program to Catch Multiple Exceptions in One Line
# Python Program to Copy a File
# Python Program to Concatenate Two Lists
# Python Program to Check if a Key is Already Present in a Dictionary
# Python Program to Split a List Into Evenly Sized Chunks
# Python Program to Parse a String to a Float or Int
# Python Program to Print Colored Text to the Terminal
# Python Program to Convert String to Datetime
# Python Program to Get the Last Element of the List
# Python Program to Get a Substring of a String
# Python Program to Print Output Without a Newline
# Python Program Read a File Line by Line Into a List
# Python Program to Randomly Select an Element From the List
# Python Program to Check If a String Is a Number (Float)
# Python Program to Count the Occurrence of an Item in a List
# Python Program to Append to a File
# Python Program to Delete an Element From a Dictionary
# Python Program to Create a Long Multiline String
# Python Program to Extract Extension From the File Name
# Python Program to Measure the Elapsed Time in Python
# Python Program to Get the Class Name of an Instance
# Python Program to Convert Two Lists Into a Dictionary
# Python Program to Differentiate Between type() and isinstance()
# Python Program to Trim Whitespace From a String
# Python Program to Get the File Name From the File Path
# Python Program to Represent enum
# Python Program to Return Multiple Values From a Function
# Python Program to Get Line Count of a File
# Python Program to Find All File with .txt Extension Present Inside a Directory
# Python Program to Get File Creation and Modification Date
# Python Program to Get the Full Path of the Current Working Directory
# Python Program to Iterate Through Two Lists in Parallel
# Python Program to Check the File Size
# Python Program to Reverse a Number
# Python Program to Compute the Power of a Number
# Python Program to Count the Number of Digits Present In a Number
# Python Program to Check If Two Strings are Anagram
# Python Program to Capitalize the First Character of a String
# Python Program to Compute all the Permutation of the String
# Python Program to Create a Countdown Timer
# Python Program to Count the Number of Occurrence of a Character in String
# Python Program to Remove Duplicate Element From a List
# Python Program to Convert Bytes to a String


#  ### Continue,Break and Pass

# In[412]:


d=['Henry','Harry','Joy','Jessica','Jinnie','janet']
for i in d:
    if i.endswith('a'):
        break
    else:
        print(i)


# In[413]:


d=['Henry','Harry','Joy','Jessica','Jinnie','janet']
for i in d:
    if i.endswith('a'):
        continue
    else:
        print(i)


# In[414]:


d=['Henry','Harry','Joy','Jessica','Jinnie','janet']
for i in d:
    if i.endswith('a'):
        pass
    else:
        print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




