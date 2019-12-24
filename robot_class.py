from plane_class import Plane
from manipulator_class import Manipulator
class Robot_class():
    def __init__(self, params):
    
        self.plane1 = Plane([])
        self.plane2 = Plane([])
        self.plane3 = Plane([])
    def execute(self):
        print("-robot")
        self.plane1.execute()
        self.plane2.execute()
        self.plane3.execute()

odroid_1 = Robot_class([])
odroid_1.execute()