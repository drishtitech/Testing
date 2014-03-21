class Facto:
        def __init__(self,n):
          self.number=n
        def Fact(self,number=True):
            if number:
                if(number==1):
                  return 1
                else:
                  number=self.Fact(number-1)*number
                  return number
            else:
               if(number==1):
                  return 1
               else:
                  number=self.Fact(number-1)*number
                  return number
