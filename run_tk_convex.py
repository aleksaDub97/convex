#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon
from math import sqrt


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()

print("Точки прямой:")
R2Point.fp1 = R2Point()
R2Point.fp2 = R2Point()

x1, x2 = R2Point.fp1.x, R2Point.fp2.x
y1, y2 = R2Point.fp1.y, R2Point.fp2.y
x3 = 10
x4 = -10
try:
    y3 = (x3 - x1)*(y2 - y1)/(x2 - x1) + y1
    y4 = (x4 - x1)*(y2 - y1)/(x2 - x1) + y1
except(ZeroDivisionError):
    x3 = R2Point.fp1.x
    x4 = R2Point.fp2.x
    y3 = R2Point.fp1.y + 10
    y4 = R2Point.fp2.y - 10
try:
    c = sqrt((y3 - y4)**2 + (x3 - x4)**2)/(y4-y3)
except(ZeroDivisionError):
    c = 1
tk.draw_rline(R2Point(x3, y3 + c), R2Point(x4, y4 + c))
tk.draw_rline(R2Point(x3, y3 - c), R2Point(x4, y4 - c))

print("\nТочки плоскости")
try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        tk.draw_rline(R2Point(x3, y3 + c), R2Point(x4, y4 + c))
        tk.draw_rline(R2Point(x3, y3 - c), R2Point(x4, y4 - c))
        print(f"S = {f.area()}, P = {f.perimeter()}, count = "
              "{f.count_vertex()}")
except(EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
