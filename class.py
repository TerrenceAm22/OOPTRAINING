# Parent Class
class Bird:
    def __init__(self):
        print("Bird is ready")
    
    def whoisthis(self):
        print("bird")
    
    
    def swim(self):
        print("Swim faster")

# Child Class
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    
    def whoisthis(self):
        print("Penguin")
    
    def run(self):
        print("Run Faster")








# peggy = Penguin()

# peggy.whoisthis()
# peggy.swim()
# peggy.run()






class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("penguin can't fly")
    
    def swim():
        print("Penguin can swim")


#Common interface

def flying_test(bird):
    bird.fly()


#Obbjects

blu = Parrot()
peggy = Penguin()


# Passing the object
flying_test(blu)
flying_test(peggy)

