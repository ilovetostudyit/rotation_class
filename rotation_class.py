import math
from collections import OrderedDict
from operator import itemgetter

class Rotation():
    def __init__(self, params):
        self.sides_dict = {"0": 15,
                            "1": 105,
                            "2": 135,
                            "3": 225,
                            "4": 255,
                            "5": 345}
        self.dist_to_side = {}
        self.norm_sides_dict = {}
        self._params = params
        self.cur_angle = self._params["cur_angle"]
        self.cur_x, self.cur_y = self._params["cur_x"], self._params["cur_y"]
        self.bocal_array = self._params["bocal_array"]
        self.robot_rad = self._params["robot_rad"]
        self.angle_between_manip = self._params["angle_between_manip"]
    @staticmethod
    def is_task_for(name=str):
        return 'Rotation' == name
    def get_move(self, side):
        if side > 0:
            self.cur_x += math.ceil(math.sin(math.radians(self.angle_between_manip)) * self.robot_rad)
        else:
            self.cur_x -= math.ceil(math.sin(math.radians(self.angle_between_manip)) * self.robot_rad)
        self.cur_y += math.ceil(math.cos(math.radians(self.angle_between_manip)) * self.robot_rad)
        return(self.cur_x, self.cur_y)
    ##get nearest manipulator in the side
    def get_nearest_side(self):
        for side in self.sides_dict:
            self.dist_to_side[side] = self.sides_dict[side] - self.cur_angle
            self.norm_sides_dict[side] = math.fabs(self.dist_to_side[side])
        self.norm_sides_dict = OrderedDict(sorted(self.norm_sides_dict.items(), key=itemgetter(1)))
        for side in self.norm_sides_dict:
            if ((self.bocal_array[int(side)]).count(0) >= 1):
                #print("i've need to turn " + str(self.dist_to_side[side]))
                value = int(side) / 2
                #print(str(value))
                return (side, self.dist_to_side[side])
                break
    def execute(self):
        side, angle = self.get_nearest_side()
        if side:
            self.get_move(self.sides_dict[side])
        return(self.cur_x, self.cur_y, angle, side)

robot_rad = 10
angle_between_manip = 15.0
cur_x, cur_y, cur_angle = 0, 0, 250
next_x, next_y = 0, 0
bocal_array = [[0], [1], [1], [1], [0], [0]]
params = {"cur_x": cur_x,
          "cur_y": cur_y,
          "cur_angle": cur_angle,
          "next_x": next_x,
          "next_y": next_y,
          "bocal_array":bocal_array,
          "robot_rad": robot_rad,
          "angle_between_manip": angle_between_manip}
rotate = Rotation(params);
print(rotate.execute())