class Person:

    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f"Hi, my name is {self.name}")
class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject=subject
    def teach(self):
            print(f"{self.name} is teaching {self.subject}")
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def study(self):
        print(f"{self.name} is studying {self.grade}")
    #creating objects
t1=Teacher(name="Bran",subject="Robotics")
t1.teach()

s1=Student(name="Bran",grade="Grade 55")
s1.study()



