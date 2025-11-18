#define a class
class student:

    #define a constructor
        def __init__(self,name,score):
         self.name=name
         self.score=score

        #define a method
        def display(self):
         print(f"Name: {self.name}, Score: {self.score}")

            #define a method to check if student passes
        def check_pass(self):
            return self.score >= 50
        #create objects
s1=student(name="Bran",score=50)
s2=student(name="Gessy",score=60)
    #use methods
s1.display()
print(f"passed status: {s1.check_pass}")
print(f"passed status: {s2.check_pass}")
