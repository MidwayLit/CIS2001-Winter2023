from Polygon import Polygon
from Triangle import Triangle
from Rectangle import Rectangle
from Square import Square


def print_polygon_perimeter(polygon):
    print(f'{polygon.name} has a perimeter of {polygon.get_perimeter()}')


square = Polygon(4, "sqaure")

for side in range(4):
    square.set_side_length(side, 10)

print_polygon_perimeter(square)

triangle = Triangle("triangle")

triangle.set_side_length(0, 3)
triangle.set_side_length(1, 4)
triangle.set_side_length(2, 5)

print_polygon_perimeter(triangle)
print(f"The area of the triangle is {triangle.get_area()}")


number_of_sides = int(input("How many sides does your polygon have?"))
name = input("What is the name of your polygon")

users_polygon = Polygon(number_of_sides, name)

for side in range(number_of_sides):
    successful = False
    while not successful:
        try:
            length = int(input(f"Enter the length of side {side}:"))
            users_polygon.set_side_length(side, length)
            successful = True
        except ValueError as error:
            print(error)


print_polygon_perimeter(users_polygon)

rectangle = Rectangle("small rectangle")
rectangle.set_side_length(0, 5)
rectangle.set_side_length(1, 6)
rectangle.set_side_length(2, 7) # sets 0 and 2
rectangle.set_side_length(3, 8) # sets 1 and 3

print(f'Area of a rectangle is {rectangle.get_area()}')


some_square = Square("some square")

some_square.set_side_length(0, 5)

print(f'Area of a square is {some_square.get_area()}')
