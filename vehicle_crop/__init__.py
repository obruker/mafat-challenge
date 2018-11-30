from vehicle_crop.diagonal_crop import *
from vehicle_crop.diagonal_crop.point import Point
from math import *


def crop_vehicle(im, polygon, margins):
    points = list(map(lambda x: Point(x[0], x[1]), polygon))
    bounds = get_bounds(points)
    angle = find_angle(bounds)
    return cropWithPoints(im, angle, get_enlarged_rect(bounds, margins))


def get_bounds(points):
    ul = min(points, key=lambda p: p.x)
    points.remove(ul)
    ur = min(points, key=lambda p: p.y)
    points.remove(ur)
    lr = max(points, key=lambda p: p.x)
    points.remove(lr)
    ll = points[0]
    return [ul, ur, lr, ll]


def find_angle(rectangle):
    ul, ur, lr, ll = rectangle
    edges = [(ul, ur), (ul, ll), (ll, lr), (ur, lr)]
    longest = max(edges, key=lambda edge: math.hypot(edge[1].x - edge[0].x, edge[1].y - edge[0].y))
    longest_angle = -math.atan2(longest[1].y - longest[0].y, longest[1].x - longest[0].x)
    across = edges[(edges.index(longest) + 2) % 4]
    across_angle = -math.atan2(across[1].y - across[0].y, across[1].x - across[0].x)
    return (longest_angle + across_angle) / 2


def get_enlarged_rect(rect, d):
    angle = find_angle(rect)
    # print("degrees: " + str(math.degrees(angle)))
    if angle < 0:
        angle = pi / 2 + angle

    enlarged = [rect[0] + Point(d * cos(1.25 * pi - angle), d * sin(1.25 * pi - angle)),
                rect[1] + Point(d * cos(1.75 * pi - angle), d * sin(1.75 * pi - angle)),
                rect[2] + Point(d * cos(0.25 * pi - angle), d * sin(0.25 * pi - angle)),
                rect[3] + Point(d * cos(0.75 * pi - angle), d * sin(0.75 * pi - angle))]

    return enlarged
