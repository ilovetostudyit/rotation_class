from plane_class import Plane
from manipulator_class import Manipulator
class Robot_class():
    def __init__(self, params):
        self.planes = self.init_planes(4)
    def init_planes(self, n_planes):
        i = 1
        planes = {}
        while i <= n_planes:
            basic_str = "plane" + str(i)
            print(basic_str)
            planes[basic_str] = Plane([])
            i = i + 1
        return(planes)
    def execute(self):
        print("-robot")
        for each in self.planes:
            self.planes[each].execute()

odroid_1 = Robot_class([])
odroid_1.execute()