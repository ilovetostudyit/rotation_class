from manipulator_class import Manipulator
class Plane():
    def __init__(self, params):
        self.Manipulator1 = Manipulator([])
        self.Manipulator2 = Manipulator([])
    def execute(self):
        print("--plane")
        self.Manipulator1.execute()
        self.Manipulator2.execute()