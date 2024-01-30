import math
import numpy as np

from cmlibs.maths.vectorops import sub, dot, add, mult, cross, normalize, magnitude, axis_angle_to_rotation_matrix


def calculateLinePlaneIntersection(pt1, pt2, point_on_plane, plane_normal):
    line_direction = sub(pt2, pt1)
    d = dot(sub(point_on_plane, pt1), plane_normal) / dot(line_direction, plane_normal)
    intersection_point = add(mult(line_direction, d), pt1)
    if abs(dot(sub(point_on_plane, intersection_point), plane_normal)) < 1e-08:
        return intersection_point

    return None


def calculateExtents(values):
    """
    Calculate the maximum and minimum for each coordinate x, y, and z
    Return the max's and min's as:

     [x_min, x_max, y_min, y_max, z_min, z_max]

    """
    x_min = 0; x_max = 1
    y_min = 0; y_max = 1
    z_min = 0; z_max = 2
    if values:
        initial_value = values[0]
        x_min = x_max = initial_value[0]
        y_min = y_max = initial_value[1]
        z_min = z_max = initial_value[2]
        for coord in values:
            x_min = min([coord[0], x_min])
            x_max = max([coord[0], x_max])
            y_min = min([coord[1], y_min])
            y_max = max([coord[1], y_max])
            z_min = min([coord[2], z_min])
            z_max = max([coord[2], z_max])

    return [x_min, x_max, y_min, y_max, z_min, z_max]


def calculatePlaneNormal(pt1, pt2, pt3):
    dir_1 = sub(pt2, pt1)
    dir_2 = sub(pt3, pt1)
    cross_vec = cross(dir_1, dir_2)
    return normalize(cross_vec)


def calculate_centroid(data_points):
    actual_points = np.array(data_points).transpose()
    centroid = np.mean(actual_points, axis=1, keepdims=True)
    centroid = centroid.flatten()

    return centroid


def calculate_rotation_matrix(vector_1, vector_2):
    normal_dot_product = dot(vector_1, vector_2)
    normal1_length = magnitude(vector_1)
    normal2_length = magnitude(vector_2)
    theta = math.acos(normal_dot_product / (normal1_length * normal2_length))

    return axis_angle_to_rotation_matrix(cross(vector_2, vector_1), theta)


# define PEP8 compliant names.
calculate_line_plane_intersection = calculateLinePlaneIntersection
calculate_plane_normal = calculatePlaneNormal
