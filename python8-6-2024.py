#inheritance we can reuse the code how many times we want 

# Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface.


#single inheritance  
class parent:
    def function(self):
            return print("i am parent")
    
class child(parent):
    def function1(self):
            return print("i am child")
    
chi=child()

#chi.function1()
#chi.function()




class parent:
    def function(self):
            return print("i am parent")
    
class child(parent):
    def function1(self):
            return print("i am child")
    
    def function(self):
          super().__init__()                    #using this funciton will help to print the output present inside the child class
          return print("i am son of my parent")
chil=child()

#chil.function1()
#chil.function()


#multiple inheritance 

class friend1:
      friend1n="aditya"
      def friend1(self):
            return self.friend1n
      
class friend2:
      frined2n="karthik"
      def friend2(self):
            return self.frined2n
    
class friend(friend1,friend2):
      def friendn(self):
            return print(f"sriram friends are {self.friend1n} and {self.frined2n}")
      
fri=friend()
fri.friendn()



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


#SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.

#TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.

#NameError: This exception is raised when a variable or function name is not found in the current scope.

#IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.

#KeyError: This exception is raised when a key is not found in a dictionary.

#ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.

#AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.

#ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.

#ImportError: This exception is raised when an import statement fails to find or load a module.

