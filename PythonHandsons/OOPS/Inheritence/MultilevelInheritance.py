class Calc1:
    def sum(self,a,b):
        return  a + b
class Calc2:
    def sub(self,a,b):
        return a - b

class Calc3:
    def mul(self,a,b):
        return a * b


class Derived(Calc1,Calc2,Calc3):
    def Devide(self,a,b):
        return a / b

d =Derived()
print(d.mul(10,20))
print(d.sum(10,20))
print(d.sub(10,20))
print(d.Devide(10,20))
