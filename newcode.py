#variables
"""

name = "roy"
age = 22
price = 22.33
print(name,",",age,",",price)  // roy 22 22.33
print("my name is",name)  // my name is roy
x=1
y=3
sum = x+y
print(sum) // 4

"""
#data types
"""
name = "roy"
age = 22
price = 22.33
print(type(price)) // float
print(type(True)) // bool
a= None
print(type(a)) // <class 'NoneType'> 

"""
#keywords
"""
we cannot use keywords as a variables.
list of keywords=
and,as,assert,break,class,continue,def,del,elif,else,except,finally,False
for,from,global,if,import,in,is,lambda,noniocal,None,not,or,pass,raise
return,True,try,with,while,yield

"""
# operators
"""
Arithmetic operator=(+ - * / % **) in division answer is always float
 **= raise to the power 
Relational or comparision operatot = (== != > < >= <=) output will be boolean
Assignment operators = (= += -= /= %= **=) 
Logical operator ( not and or)
 print(not False) // True
or gives false only when both are false
and gives true only when both are true
\n = for changing line
"""
#type casting and conversion
"""
Type Conversion

a, b = 1, 2.0
sum = a + b int can be type converted to float

#error
a, b = 1, "2"
sum = a + b string cannot be type converted to float

Type Casting

a, b = 1, "2"
c = int(b)

sum = a + c
 we type casted string into integer

"""
#inputs
"""
input( ) statement is used to accept values (using keyboard) from user
input( ) #result for input( ) is always a str
float ( input( ) ) #float
int ( input( ) ) #int
name = input("enter your name :")

"""

#strings
"""
len(str) // length of string str
concatenation "he" + "r" gives her
if one string has value 2 and other has 3 and if we add them it will give 23.

Indexing str=roy where str[0]=r
str[0]=t is not allowed

Slicing
str = kaushal
str[1:4] is aus
str[:4] is kaus here blank space is "0"
str[1:] is aushal here blank space is length of string
str[-7:-1] is kausha because in negetive indexing l is -1 and then a is -2 and so on

 Functions in string
str.endsWith(“er.“) #returns true if string ends with er
str.capitalize( ) #capitalizes 1st char
str.replace( old, new ) #replaces all occurrences of old with new
str.find( word ) #returns 1st index of 1st occurrence
str.count(“am“) #counts the occurrence of substr in string

"""
#conditional statements
"""
if-elif-else (SYNTAX)

if condition :

Statement1

elif condition:

Statement2

else:

StatementN

//can use as many as elif as you want even zero...
// proper spacing is must for execution
 
 Nesting
 if ke andar ek aur  if
 
"""
#List of python = arrays of c or c++   []
"""
it is muttable
A built-in data type that stores set of values
It can store elements of different types (integer, float, string, etc.)
marks = [87, 64, 33, 95, 76]#marks[0], marks[1]..
student = [”Karan”,85,“Delhi”] #student[0], student[1]..
student[0] =“Arjun” #allowed in python
len(student) #returns length

List slicing same as of string slicing

List methods
list = [2, 1, 3]
list.append(4) #adds one element at the end [2,1,3,4]
list.insert( idx, el ) #insert element at index
list.sort( ) #sorts in ascending order [1,2,3]
list.reverse( ) #reverses list [3,1,2]
list.sort( reverse=True ) #sorts in descending order [3,2,1]
list.copy // gives us copy of the list

list = [2, 1, 3, 1]
list.remove(1) #removes first occurrence of element [2,3,1]
list.pop( idx ) #removes element at idx
list(any data) //converting into list

"""
#Tuples ()
"""
it is immutable not like list where we can change objects easily by using index
tup = (87, 64, 33, 95, 76) 
tup =() //empty tuple
tup = (1,)// if we have only one object use comma after object

Tuple methods
tup = (2, 1, 3, 1)
tup.index( el ) #returns index of first occurrence  tup.index(1) is 1
tup.count( el ) #counts total occurrences  tup.count(1) is 2
we can convert tuple into list
lis = list(tup) 
print(tup[1]) //1

"""
#dictionary {}
"""
they are unordered, mutable and duplicate keys cannot be used
dict1 ={
"key" : value,  //key and value can be anything string int bool float tuple list etc.
}

print(dict1(key))  //value will be printed and if key dosent exist then it will return error
dict1("key")=value1 //value can be changed
dict1("newkey")=value2 // new key added
empty dictionary can also be created
we can use key of dictionay as new dictionary it is called nesting in dictionary

Dictionary methods
Dict.keys( ) #returns all keys
Dict.items( ) #returns all (key, val) pairs as tuples
Dict.update( newDict ) #inserts the specified items to the dictionary // we can add key and value pair in dictionary by this method using new dictionary or by adding just new pair
Dict.values( ) #returns all values
Dict.get( “key““ ) #returns the key according to value // if key doesnt exist then it will return none not error


"""
#sets {} 
"""
unoredered items,unique elements and immutable
list and dictionary can not be stored in set as they are mutable
if duplicate values are stored then it will be ignored 

Set Methods
set.add( el ) #adds an element
set.remove( el ) #removes the elemant
set.clear( ) #empties the set
set.pop( ) #removes a random value

set.union( set2 ) #combines both set values & returns new
set.intersection( set2 ) #combines common values & returns new

"""
#loops
"""
While loop
 while condition:
   #statement

 Break // it terminates the loop
 Continue // terminates execution in the current iteration & continues execution of the loop
with the next iteration

For else loop // used for sequential traversal. For traversing list, string, tuples etc.
for el in list:
#some work
else:
#work when loop ends
 
Range()
range(start , stop , step) //Range functions returns a sequence of numbers, starting from 0 by default, and increments by
1 (by default if we donot give step), and stops before a specified number 
range(5) // 0,1,2,3,4
range(1,5) //1,2,3,4
range(1,10,2) //1,3,5,7,9
seq = range(1,10,2) // seq[3]=7
 
Pass
 pass is a null statement that does nothing. it is used as a placeholder for future code
 for el in list:
  pass  // we need to write code below for loop otherwise it gives error so for the time we dont have code then write pass


"""
#Functions
"""
Block of statements that perform a specific task.it takes some input and returns some output.
def funcname(arg1, arg2):
    #somework
    return val
if we want arg value to be constant then write it while making the func
def fun(arg1,arg2=2):  // arg 2 ki value const ho gayi

while using print in loop if we want every word in single line then do
print(jo bhi likho,end=" ")

Recursion
When a function calls itself repeatedly
example-
def show(n):
   if(n==0):  //base case
        return
    print(n)
    show(n-1)    

 example2-
 def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)          

"""
#files i/o
"""
python can be used to perform operations on a file .(read & write data)

text files :.txt, .docx,.log etc.
binary files : .mp4,.mov,.png,.jpeg etc

we have to open a file before reading or writing

f=open(""filename","mode")
filename = name.txt or name.docx etc
mode = r-for reaad mode  //if mode not mentioned then its readmode
       w-for writing in file and deleting old data
       a-writing the file without deleting the data
       b-binary mode
       t-text mode
       +-open a disk file for updating (readin and writing)
       r+-read+write but new data is written in the starting
       w+-read+write but delets old data
       a+-read+write but new data is written in the ending
data = f.read(a) //number of char to read if its not mentioned then whole file will be read.
 f.close() // always close your file its sign of good coder
//if file is not in same folder as file we are writing our code is then we have to give full path.

Reading file
data=f.readline() //reads one line at a time.

Writing file
f=open("filename","w")
f.write("add kr lines")//but it will delete old data

f=open("filename","a")
f.write("add kr lines")//not data loss only adds data
 
With syntax // another type of writing code and no need to close file here
withopen("filename","a")as f:
data = f.read()

Deleting a file
using the os module
module (like a code library)is a file written by another programmer that generally has a function we can use
import os
os.remove("file name")


"""
#OOPs 
"""
Learn with example
class Car:
   def __init__(self,brand,model):
    self.brand = brand
    self.model = model

mycar = Car("toyota","corolla")
mycar2= Car("honda","city")
print(mycar2.brand,mycar2.model) // honda city 

Method //
class Car:
   def __init__(self,brand,model):
    self.brand = brand
    self.model = model
   def fullname(self):
    print(self.brand,self.model)

Inheritance // when you want to make a new class by adding some new attributes to the old class
class newcar(Car):
    def __init__(self,brand,model,batterysize):
       super().__init__(brand,model)
       self.batterysize=batterysize

tesla = newcar("tesla","model s","85kwh")
print(tesla.model,tesla.batterysize)
 
Encapsulation //





"""

""" c, a, b = map(int, input().split()) // can take input in this way also and its usefull when you wanna take input in a single line
"""

