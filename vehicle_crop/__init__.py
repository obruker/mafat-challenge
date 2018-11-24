from vehicle_crop.diagonal_crop import *
from vehicle_crop.diagonal_crop.point import Point
from math import *

def crop_vehicle(im, points, margins):
    rect = get_rotated_points(points)
    angle = find_angle(rect)
    # print(rect)
    return cropWithPoints(im, angle, get_enlarged_rect(rect, margins))

def get_rotated_points(points):
    ul = min(points, key=lambda p:p.x)
    points.remove(ul)
    ur = min(points, key=lambda p:p.y)
    points.remove(ur)
    lr = max(points, key=lambda p:p.x)
    points.remove(lr)
    ll = points[0]
    return [ul,ur,lr,ll]

def find_angle(rect_points):
    ul, ur, lr, ll = rect_points
    # edges = [(ul,ur),(ul,ll),(ll,lr),(ur,lr)]
    edges = [(ul,ur),(ul,ll)]
    longer = max(edges, key=lambda edge: math.hypot(edge[1].x-edge[0].x, edge[1].y-edge[0].y))
    return -math.atan2(longer[1].y - longer[0].y, longer[1].x - longer[0].x)

def get_enlarged_rect(rect, d):
    angle = find_angle(rect)
    # print("degrees: " + str(math.degrees(angle)))
    if angle < 0:
        angle = pi/2 + angle

    # dx = d * cos(1.25*pi - angle)
    # dy = d * sin(1.25*pi - angle)
    # print("dx: " + str(dx))
    # print("dy: " + str(dy))
    enlarged = [rect[0] + Point(d * cos(1.25*pi - angle), d * sin(1.25*pi - angle)),
                rect[1] + Point(d * cos(1.75*pi - angle), d * sin(1.75*pi - angle)),
                rect[2] + Point(d * cos(0.25*pi - angle), d * sin(0.25*pi - angle)),
                rect[3] + Point(d * cos(0.75*pi - angle), d * sin(0.75*pi - angle))]

    # print(enlarged)
    return enlarged
