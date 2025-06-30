
class Rectangle:

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def result(self):
        print(self.side_a * self.side_b)

total = Rectangle(4, 5)
total_two = Rectangle(6, 5)

total.result()
total_two.result()