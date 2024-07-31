class constructor:
    def __init__(self,name,course): #constructor
        self.name=name
        self.course=course

    def view(self):
        print("name:",self.name)
        print("course:",self.course)
co=constructor("tarun","python")
co.view()