class Student:
    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def display(self):
        
        print(f"{self.name}",end="\t\t")
        print(f"{self.age}",end="\t\t")
        print(f"{self.rollno}")
lis=[]
n=int(input("Enter no of students :"))
for i in range(n):
    print("Student-",i+1)
    name=input("Enter the name :")
    age=int(input("Enter age :"))
    rollno=input("Enter roll number: ")
    lis.append(Student(name,age,rollno))
    print()
print("Name\t\tAge\t\tRollnumber")
print(" ")
for i in range(len(lis)):
    lis[i].display()
