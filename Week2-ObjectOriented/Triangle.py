import math

from Polygon import Polygon

class Triangle(Polygon):

    def __init__(self, name=""):
        #Polygon.__init__(self)
        super().__init__(3, name)

    def get_area(self):
        # https://byjus.com/maths/area-of-a-triangle/
        semi_perimeter = self.get_perimeter() / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter-self.get_side_length(0))
                         * (semi_perimeter-self.get_side_length(1))
                         * (semi_perimeter-self.get_side_length(2)))