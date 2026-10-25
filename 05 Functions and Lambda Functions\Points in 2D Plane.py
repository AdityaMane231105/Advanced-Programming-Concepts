import math

points = [(2, 3), (5, 7), (1, 1)]

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def farthest_from_origin(points):
    return max(points, key=lambda p: math.sqrt(p[0]**2 + p[1]**2))

print("Distance:", distance(points[0], points[1]))
print("Farthest:", farthest_from_origin(points))
