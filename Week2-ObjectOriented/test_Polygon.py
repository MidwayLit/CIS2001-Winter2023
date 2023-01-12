from unittest import TestCase
from Polygon import Polygon

class TestPolygon(TestCase):

    def test_polygon_init(self):
        # Arrange
        # Arrange the code we are going to test - setup the variables we need
        expected_number_of_sides = 5
        expected_name = 'pentagon'
        some_polygon = Polygon(expected_number_of_sides, expected_name)

        # Act - call the code we are testing
        actual_number_of_sides = some_polygon.get_number_of_sides()
        actual_name = some_polygon.name

        # Assert - did we get what we expected?
        self.assertEqual(expected_number_of_sides, actual_number_of_sides)
        self.assertEqual(expected_name, actual_name)

    def test_get_number_of_sides(self):
        # AAA convention

        # Arrange the code we are going to test - setup the variables we need
        expected_number_of_sides = 5
        some_polygon = Polygon(expected_number_of_sides)

        # Act - call the code we are testing
        actual_number_of_sides = some_polygon.get_number_of_sides()

        # Assert - did we get what we expected?
        self.assertEqual(expected_number_of_sides, actual_number_of_sides)



    def test_set_side_length(self):
        # Arrange the code we are going to test - setup the variables we need
        expected_number_of_sides = 4
        some_polygon = Polygon(expected_number_of_sides)
        expected_perimeter = 10
        expected_side_lengths = [1,2,3,4]

        # Act - call the code we are testing
        for side_index in range(4):
            some_polygon.set_side_length(side_index, side_index+1)

        # duplicate for example
        some_polygon.set_side_length(0, 1)
        some_polygon.set_side_length(1, 2)
        some_polygon.set_side_length(2, 3)
        some_polygon.set_side_length(3, 4)

        actual_side_lengths = []
        for side_index in range(4):
            actual_side_lengths.append(some_polygon.get_side_length(side_index))

        actual_perimeter = some_polygon.get_perimeter()

        # Assert - did we get what we expected?
        self.assertEqual(expected_perimeter, actual_perimeter)
        self.assertListEqual(expected_side_lengths, actual_side_lengths)

