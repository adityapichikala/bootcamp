# in input and output statements can be directly taken inside print statement  
#print(input("enter number:"))
#we can use sep and end inside print statement sep is used for specifing space and end is used for printing side ways these are keyword arguments 

#data types in python
int_num = 3
float_num = 3.33
complex_num = 3 + 3j
string = "Aditya"
boolean = True
list_example = [2,5,6,37,74]
tuple_example = (3,6,2,7,8,4)
dict_example = {"name": "Aditya", "age": 18}
set_example = {9,8,3,7,4,1,5}

#Arithmetic Operators
#+,-,*,/,//,%,**

#Comparision operators
#==,>=,<=,!=,>,<

#logical operators  gives bool as output
#and,or with >,< ,not

#Type casting
#type casting means changing of datatypes from one form to another 

#conditional statements 
'''
a=30
b=50
if a>b:
    print("True")
elif a<b:
    print("False")
'''

#looping statements
# there are two types of loops - 1.for 2.while 
#while loop is also know as infinite loop

#special functions
'''
there are few special functions which are used in code like len(),id(),type()

len()  functions is used to find the number of characters present 
id() is used for itdentifing any object
type() is used to find what kind of datatype it is 
'''

#Area calculator 
def rectangle(length,breadth):
    return  length*breadth
    
def circle(radius):
     return radius*radius
    
print(rectangle(2,4))
print(circle(5))


#reverse string
def reversed(x):
     q=x.split()
     
     w=q[::-1]

     return " ".join(w)
#y=input("enter string:")
#print(reversed(y))

#list statistics

def lis(x):
    mini=min(x)
    maxi=max(x)
    avge=sum(x)/len(x)
    li={
          "minimum":mini,
          "maximum":maxi,
          "average":avge
     
     }
    return li
#x=list(map(int,input("enter numbers: ").split()))
#print(lis(x))


#filtering with lambda

def qwwe(x,y):
     qwerty=list(filter(lambda x:len(x)<y,x))
     return qwerty
    
#x=list(input("-->").split())
#y=8
#print(qwwe(x,y))


q=input("enter:").split()
e=list(q)
w=len(q)
char_count = len("".join(q))
print(char_count)