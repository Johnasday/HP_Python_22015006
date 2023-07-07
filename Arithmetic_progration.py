class Series:
    def __init__(self, number):
        self.number=number 
    def __init__(self, number):
        self.number = (self)
class ArithmeticOps:
    def __init__(self, total):
        self._total = total
        print('creating a new instance')
    
    def __repr__(self):
        return f"ArithmeticOps(total={self._total})"
    
    def __add__(self, value):
        return ArithmeticOps(self._total + value)
        
    def __iadd__(self, value):
        self._total += value
        return self


a = ArithmeticOps(20)   


for i in range(1,4):
    a += i
    print(a)
    
print('after loop a =', a)
