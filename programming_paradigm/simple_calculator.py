class SimpleCalculator:
    def add (self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def devide(self,a,b):
        if b==0:
            return None
        else:
            return a/b
    