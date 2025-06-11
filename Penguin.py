# parent class:

class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def WhoIsThis(self):
        print("Bird in parent")

    def swim(self):
        print("Swim faster!")

# child class

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def WhoIsThis(self):
        print("Penguin")
    
    def run(self):
        print("Run faster")

# Object creation:

peggy = Penguin()
peggy.WhoIsThis()
peggy.swim()
peggy.run()
