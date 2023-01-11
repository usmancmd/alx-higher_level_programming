#!/usr/bin/python3
"""Defines a pascal triangle function"""


def pascal_triangle(n):
    """returns a list of integers inform of Pascal’s triangle"""
    if n < 0:
        return []
    else:
        triangles = [[1]]
        while len(triangles) != n:
            triangle = triangles[-1]
            temp = [1]
            for i in range(len(triangles) - 1):
                temp.append(triangle[i] + triangle[i + 1])
            temp.append(1)
            triangles.append(temp)
    return triangles
