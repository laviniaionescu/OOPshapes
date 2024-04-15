import math
class Shape:
    def __init__(self):
        pass

######################################################


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

# rectangle = Rectangle(2,2)
# area = rectangle.calculate_area()
# perimeter = rectangle.calculate_perimeter()
# print(f"The area of the rectangle is {area}")
# print(f"The perimeter of the rectangle is {perimeter}")


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def calculate_area(self):
        area = self.side ** 2
        return area

    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter

# square = Square(3)
# area = square.calculate_area()
# perimeter = square.calculate_perimeter()
# print(f"The area of the square is {area}")
# print(f"The perimeter of the square is {perimeter}")

######################################################


class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def calculate_area(self):
        semi_peri = (self.side_a + self.side_b + self.side_c) * 1/2
        area = math.sqrt(semi_peri *
                         (semi_peri - self.side_a) *
                         (semi_peri - self.side_b) *
                         (semi_peri - self.side_c))
        return area

    def calculate_perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter


# triangle = Triangle(5,5,6)
# area = triangle.calculate_area()
# perimeter = triangle.calculate_perimeter()
# print(f"The area of the triangle is {area}")
# print(f"The perimeter of the triangle is {perimeter}")


class RightTriangle(Triangle):
    def __init__(self, side_a, side_b, hypotenuse):
        super().__init__(side_a, side_b, hypotenuse)

    def calculate_area(self):
        area = (self.side_a * self.side_b) * 1/2
        return area

    def calculate_perimeter(self):
        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter


# right_triangle = RightTriangle(3,6,6.7)
# area = right_triangle.calculate_area()
# perimeter = right_triangle.calculate_perimeter()
# print(f"The area of the right triangle is {area}")
# print(f"The perimeter of the right triangle is {perimeter}")

######################################################

