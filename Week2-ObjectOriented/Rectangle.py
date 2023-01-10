from Polygon import  Polygon


class Rectangle(Polygon):

    def __init__(self, name=""):
        super().__init__(4, name)

    def get_area(self):
        return self.get_side_length(0) * self.get_side_length(1)

    def set_side_length(self, side_index, length):
        # odd sides
        if side_index % 2:
            super().set_side_length(1, length)
            super().set_side_length(3, length)
        else:
            super().set_side_length(0, length)
            super().set_side_length(2, length)
