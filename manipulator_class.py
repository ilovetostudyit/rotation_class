class Manipulator():
    def __init__(self, params):
        self._params = params
        self.manip_name = self._params["name"]
        self.plane_num = self._params["plane_num"]
        self.rel_manip_num = self._params["manip_num"]
        self.n_manips = self._params["n_manips"]
        self.between_plane_angle = self._params["between_plane_angle"]
        self.manip_center_angle = self._params["manip_center_angle"]
        self.abs_manip_num = self.get_abs_manip_num()
        self.manip_angle = self.get_manip_angle()

    def get_abs_manip_num(self):
        return((self.plane_num - 1) * self.n_manips + (self.rel_manip_num - 1))
    def get_manip_angle(self):
        base = -15
        if (self.rel_manip_num % 2 == 0):
            plane_even = 1
        else:
            plane_even = 0
        print((self.manip_center_angle * 2 + self.between_plane_angle) * (self.plane_num - 1) + base + plane_even * self.manip_center_angle * 2)
        get_angle = (self.manip_center_angle * 2 + self.between_plane_angle) * (self.plane_num - 1) + base + plane_even * self.manip_center_angle * 2
        if get_angle < 0:
            get_angle = 360 + get_angle
        return(get_angle) 
    def execute(self):
        print("---manip " + str(self.abs_manip_num) + " (plane " + str(self.plane_num) + " manip " + str(self.rel_manip_num) + ")")
        print("----angle of manip: " + str(self.manip_angle))