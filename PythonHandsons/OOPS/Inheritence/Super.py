
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def prineName(self):
        print(self.fname,self.lname)


class Student(Person):
    def __init__(self,year,fname,lname):
        super().__init__(fname,lname)
        self.graduationYesr = year

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
myclass = MyNumbers()
myiter = iter(myclass)
