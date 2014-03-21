class Shape:
    def area(self,x,y):
      a1=x*y
      print "Area of Rectangle is:",a1  
      return
    def area1(self,x):
      a2=x*x
      print "Area",a2
      return
class Rectangle(Shape):
    #def display():
      #return True
    pass
    
b=Rectangle() 
b.area(10,20)
b.area1(10)      
