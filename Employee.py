# Parent Class:

class Person(object):
    
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber 

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class:

class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

    # invoking the __ init __ of the parent class:
        Person.__init__(self, name, idnumber)

# creation of an object or variable ir an instance

a = Employee('Rahul', 886012, 200000, 'Intern')

# calling the function via instance
a.display()
