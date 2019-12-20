from manipulator_class import Manipulator
class Plane():
    def __init__(self, params):
        self._params = params
        self.plane_name = self._params["name"]
        self.plane_num = self._params["plane_num"]
        self.n_manips = self._params["n_manips"]
        self.manip_center_angle = self._params["manip_center_angle"]
        self.between_plane_angle = self._params["between_plane_angle"]
        #print(str(self.between_plane_angle))
        #print(self.plane_name)
        self.manipulators = self.init_manipulators()
    def init_manipulators(self):
        i = 1
        manipulators = {}
        while i <= self.n_manips:
            basic_str = "manip" + str(i)
            plane_dict = {"name": basic_str,
                          "plane_num": self.plane_num,
                          "manip_num": i,
                          "n_manips": self.n_manips,
                          "manip_center_angle": self.manip_center_angle,
                          "between_plane_angle": self.between_plane_angle}
            manipulators[basic_str] = Manipulator(plane_dict)
            i = i + 1
        return(manipulators)
    def execute(self):
        i = 1
        print("--" + str(self.plane_name))
        while i <= self.n_manips:
            self.manipulators["manip" + str(i)].execute()
            i = i + 1