class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisthis(self):
       print("Bird")
    def swim(self):
        print("swim faster")
class penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisthis(self):
        print("Penguin")
    def run(self):
        print("run faster")
peggy = penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()
    
      
    
    
    
