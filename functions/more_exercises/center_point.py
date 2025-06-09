
import math

points = tuple(math.floor(float(input())) for _ in range(4))
sum_x = sum(abs(num) for num in points[:2])
sum_y = sum(abs(num) for num in points[2:])


def whats_closer(arg1, arg2):
    return points[:2] if arg1 <= arg2 else points[2:]


print(whats_closer(sum_x, sum_y))
# x1 = float(input())
# y1 = float(input())
# point_one = (x1, y1)
#
# x2 = float(input())
# y2 = float(input())
# point_two = (x2, y2)
#
# def coordinate(point_one, point_two):
#
#     if point_one < point_two:
#         if point_one < 0 and point_two < 0:
#             print(f'({x1:.0f}, {y1:.0f})')
#     else:
#         print(f'({x2:.0f}, {y2:.0f})')
#
# coordinate(point_one, point_two)