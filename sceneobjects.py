# simple3d.py

import open3d as o3d
import numpy as np

class Point:
    def __init__(self, coords):
        self.coords = np.array(coords, dtype=float)

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

class Scene:
    def __init__(self):
        self.points = []
        self.lines = []

    def add(self, obj):
        if isinstance(obj, Point):
            self.points.append(obj)
        elif isinstance(obj, Line):
            self.lines.append(obj.start)
            self.lines.append(obj.end)
        else:
            raise TypeError("Unsupported object type")

    def show(self):
        unique_points, index_map = self._get_unique_points()
        line_indices = self._build_line_indices(index_map)

        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(unique_points)

        line_set = o3d.geometry.LineSet()
        line_set.points = o3d.utility.Vector3dVector(unique_points)
        line_set.lines = o3d.utility.Vector2iVector(line_indices)

        o3d.visualization.draw_geometries([pcd, line_set])

    def _get_unique_points(self):
        point_map = {}
        unique_list = []
        index = 0

        for pt in self.points + self.lines:
            key = tuple(pt.coords)
            if key not in point_map:
                point_map[key] = index
                unique_list.append(pt.coords)
                index += 1

        return np.array(unique_list), point_map

    def _build_line_indices(self, point_map):
        line_indices = []
        for i in range(0, len(self.lines), 2):
            start = tuple(self.lines[i].coords)
            end = tuple(self.lines[i+1].coords)
            line_indices.append([point_map[start], point_map[end]])
        return line_indices

