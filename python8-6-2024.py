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
      def friend(self):
            return print(f"sriram friends are {self.friend1n} and {self.frined2n}")
      
fri=friend()
fri.friend()