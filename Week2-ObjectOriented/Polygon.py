class Polygon:

    def __init__(self, number_of_sides, name=""):
        self._number_of_sides = number_of_sides
        self._side_lengths = [0] * number_of_sides
        self.name = name

    def get_number_of_sides(self):
        return self._number_of_sides

    def set_side_length(self, side_index, length):
        if length <= 0:
            raise ValueError("Length must be > 0")
        self._side_lengths[side_index] = length

    def get_side_length(self, side_index):
        return self._side_lengths[side_index]

    def get_perimeter(self):
        return sum(self._side_lengths)


