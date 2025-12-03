class Engin:
    def __init__(self,power):
        self._power=power
        
class Wheels:
    def __init__(self,size):
        self._size=size


class Car(Engin,Wheels):
    def __init__(self, model,power,size):
        Engin.__init__(self,power)
        Wheels.__init__(self,size)
        self.model=model
    def display(self):
        print(f"The Model is {self.model}, The Power Of the {self.model} is {self._power}, The Wheel Size of {self.model} is {self._size}")
    
        
obj=Car("BMW","2000",20)
obj.display()        
        
        