import math
import unittest

import vehicle_crop
from vehicle_crop.diagonal_crop.point import Point


class VehicleCropTest(unittest.TestCase):

    def test_get_rotated_points(self):
        points = [Point(3988.399902,1227.588745),
                  Point(3986.710693,1213.288208),
                  Point(4002.600098,1211.411255),
                  Point(4004.289307,1225.711792)]
        expected = [points[1],points[2],points[3],points[0]]
        self.assertEquals(vehicle_crop.get_bounds(points), expected)

    def test_get_angle(self):
        points = [Point(20,10),
                  Point(30,20),
                  Point(20,30),
                  Point(10,20)]
        rect = vehicle_crop.get_bounds(points)
        self.assertEquals(vehicle_crop.find_angle(rect), math.pi / 4)

    def test_get_angle_under_45_degrees(self):
        points = [Point(10,10),
                  Point(11,1),
                  Point(30,2),
                  Point(29,12)]
        rect = vehicle_crop.get_bounds(points)
        angle = math.degrees(vehicle_crop.find_angle(rect))
        self.assertEquals(angle, math.pi / 4)

    def test_get_enlarged_rect_45degrees(self):
        rect = [Point(10,20),
                Point(20,10),
                Point(30,20),
                Point(20,30)]
        enlarged = [Point(5,20),
                    Point(20,5),
                    Point(35,20),
                    Point(20,35)]
        self.assertEquals(vehicle_crop.get_enlarged_rect(rect, 5),enlarged)

    def test_get_enlarged_rect(self):
        rect = [Point(2441.47,2035.118),
                Point(2456.478,2010.104),
                Point(2534.021,2054.295),
                Point(2519.847,2077.642)]
        degree = vehicle_crop.find_angle(rect)
        print(degree)
        d1 = 2.843
        d2 = 9.587
        enlarged = [Point(2441.47-d2,2035.118-d1),
                Point(2456.478-d1,2010.104-d2),
                Point(2534.021+d2,2054.295+d1),
                Point(2519.847+d1,2077.642+d2)]
        self.assertEquals(vehicle_crop.get_enlarged_rect(rect, 10),enlarged)
