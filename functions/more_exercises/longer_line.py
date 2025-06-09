import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

def distance(xa, ya, xb, yb):
    return math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    line1_len = distance(x1, y1, x2, y2)
    line2_len = distance(x3, y3, x4, y4)

    if line1_len >= line2_len:
        print(f'({x2}, {y2})({x1}, {y1})')
    else:
        print(f'({x4}, {y4})({x3}, {y3})')

longer_line(x1, y1, x2, y2, x3, y3, x4, y4)


# import math
#
# x1 = int(input())
# y1 = int(input())
#
# x2 = int(input())
# y2 = int(input())
#
# x3 = int(input())
# y3 = int(input())
#
# x4 = int(input())
# y4 = int(input())
#
# # point_one = (x1, y1)
# # point_two = (x2, y2)
# # point_three = (x3, y3)
# # point_four = (x4, y4)
#
# def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
#
#     one = (y2 - y1) / (x2 - x1)
#     line_one = y1 - one * x1
#     two = (y4 - y3) / (x4 - x3)
#     line_two = y3 - two * x3
#     if line_two > line_one:
#         print(f'({x2}, {y2})({x1}, {y1})')
#     else:
#         print(f'({x4}, {y4})({x3}, {y3})')
#
# longer_line(x1, y1, x2, y2, x3, y3, x4, y4)