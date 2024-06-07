#self is a special parameter that is automatically included in the definition of every method within a class.

class dev:
    def __init__(self,data):
        self.data=data
    def ican(self):
        return self.data
    
qwe=dev(5)
print(qwe.ican())


class person:
    def __init__(self,firstname,lastname):
         self.fname=firstname
         self.lname=lastname

    def printname(self):
        print(self.fname,self.lname)

x=person('aditya','karthik')
x.printname()


class rectangle:
    def rectangle1(self,height,width):
        self.height=height
        self.width=width

    def area(self):
        return self.height * self.width
    def perimeter(self):
        return 2*(self.height + self.width)
    
rec=rectangle()
rec.rectangle1(3,2)
print(f"the height and width of the rectangle are {rec.height} and {rec.width} ")
print(f"The area of the rectangle is {rec.area()}")
print(f"The perimeter of a rectangle is {rec.perimeter()}")



class circle:
    
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (3.14*self.radius*self.radius)
    def perimeter(self):
        return (2*3.14*self.radius)
    
cir=circle(9)

print(f"the radius of the circle is {cir.radius}")
print(f"the area of the circle is {cir.area()}")
print(f"the perimeter of the circle is {cir.perimeter()}")


class person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.dateofbirth=date_of_birth

    def name(self):
        return self.name
    def country(self):
        return self.country
    def date_of_birth(self):
        return self.dateofbirth
    
    def age(self):
        return (2023-self.dateofbirth)
    
per=person("aditya","india",2005)

print(f"My name is {per.name}.I am from {per.country}.My age is {per.age()}")



#inheritance 

class parent():
    def output(self):
        print("i am the parent")
class child(parent):
    def outputc(self):
        print("i am the child")
c = child()
c.outputc()
c.output()



class human:
    def work(self):
        print("i can work")
    def say(self):
        print("i can say")

class male(human):
    def speak(self):
        print("i am speak")
    def work(self):
        super().work()         
        print("i can code")

male1=male()
male1.work()




