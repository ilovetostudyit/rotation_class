from plane_class import Plane
from manipulator_class import Manipulator
class Robot_class():
    def __init__(self, params):
        self._params = params
        self.n_planes = self._params["n_planes"]
        self.n_manips = self._params["n_manips"]
        self.manip_center_angle = self._params["manip_center_angle"]
        self.between_plane_angle = self.get_between_plane_angle()
        print("::" + str(self.between_plane_angle))
        self.planes = self.init_planes(self.n_planes)
    def get_between_plane_angle(self):
        return ((360 - self.n_planes * self.n_manips * self.manip_center_angle) / self.n_planes)
    def init_planes(self, n_planes):
        i = 1
        planes = {}
        while i <= n_planes:
            basic_str = "plane" + str(i)
            plane_dict = {"name": basic_str,
                          "plane_num": i,
                          "n_manips": self.n_manips,
                          "manip_center_angle": self.manip_center_angle,
                          "between_plane_angle": self.between_plane_angle}
            planes[basic_str] = Plane(plane_dict)
            i = i + 1
        return(planes)
    def execute(self):
        print("-robot")
        for each in self.planes:
            self.planes[each].execute()
n_planes_dict =  {"n_planes": 3,
                  "n_manips": 2,
                "manip_center_angle": 15}
odroid_1 = Robot_class(n_planes_dict)
odroid_1.execute()