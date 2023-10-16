#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void, Figure

print("Точки прямой:")
R2Point.fp1 = R2Point()
R2Point.fp2 = R2Point()

print("\nТочки плоскости")
f = Void()
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, count = {f.count_vertex()}")
        print()
except(EOFError, KeyboardInterrupt):
    print("\nStop")
