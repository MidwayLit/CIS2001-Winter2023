from Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, name=""):
        super().__init__(name)

    def set_side_length(self, side_index, length):
        super().set_side_length(0, length)
        super().set_side_length(1, length)
