import random
from typing import Tuple, Optional, Set

import numpy as np

from kcenter.constant.colour import Colour


class GraphGenerator:

    @staticmethod
    def choose_colour(remaining_blue: int, remaining_red: int) -> Tuple[Optional[Colour], int, int]:
        if remaining_blue < 0 or remaining_red < 0:
            return None, remaining_blue, remaining_red
        if remaining_blue == 0 and remaining_red == 0:
            return None, remaining_blue, remaining_red
        if remaining_blue == 0:
            return Colour.RED, remaining_blue, remaining_red - 1
        if remaining_red == 0:
            return Colour.BLUE, remaining_blue - 1, remaining_red

        rand_num = np.random.uniform(0, remaining_blue + remaining_blue)
        if rand_num < remaining_blue:
            return Colour.BLUE, remaining_blue - 1, remaining_red
        else:
            return Colour.RED, remaining_blue, remaining_red - 1

    @staticmethod
    def get_random_point_around_center(opt: float, point: Tuple[int, int]):
        """Returns a uniformly random point at max distance [opt] from a given [point]

        :param opt: maximum distance away from point
        :param point: point to generate new point around
        :return:
        """
        length = np.sqrt(np.random.uniform(0, opt))
        return GraphGenerator.get_random_point_around_circumference(length, point)

    @staticmethod
    def get_random_point_around_circumference(dist: float, point: Tuple[float, float]):
        """Returns a random point the circumference of radius [opt] from a given [point]

        :param opt: distance away from point
        :param point: point to generate new point around
        :return:
        """
        angle = np.pi * np.random.uniform(0, 2)

        x = dist * np.cos(angle)
        y = dist * np.sin(angle)
        return point[0] + x, point[1] + y

    def generate_point(self):
        return random.uniform(self.min_x, self.max_x), random.uniform(self.min_y, self.max_y)

    def get_random_distanced_point(self, dist: float, points: Set[Tuple[float, float]]) -> Tuple[float, float]:
        def is_point_distanced(potential_point: Tuple[float, float]):
            for p in points:
                if np.linalg.norm(np.array(p) - np.array(potential_point)) < dist:
                    return False
            return True

        point = self.generate_point()
        while not is_point_distanced(point):
            point = self.generate_point()
        return point

    def generate_unique_point(self, points: Set[Tuple[float, float]]) -> Tuple[float, float]:
        """Generates a random point within the graph space of the GraphGenerator instance

        :param points: the generated point will not be in any point in this set (optional)
        :return: A tuple of coordinates
        """
        center_coord = self.generate_point()
        while center_coord in points:
            center_coord = self.generate_point()
        return center_coord

    def __init__(self, min_x: int, min_y: int, max_x: int, max_y: int):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

    def generate(self, b, r, num_centers, opt, num_outliers, blue_red_outliers: Optional[Tuple[int, int]] = None):
        """Generates a graph with [r + b + num_outliers] nodes with optimal cost [opt]

        :param b: number of blue points to generate within the optimal solution
        :param r: number of red points to generate within the optimal solution
        :param num_centers: number of centers
        :param opt: optimal cost
        :param num_outliers: number of points outside the optimal solution
        :param blue_red_outliers: tuple of outlier numbers for (blue, red) (optional)
        :return: Dictionary representing graph
        """
        if r + b < 2 * num_centers:
            raise ValueError("Total points on graph must be larger than twice the number of centers")
        if blue_red_outliers is not None:
            if blue_red_outliers[0] + blue_red_outliers[1] != num_outliers:
                raise ValueError("Number of red and blue outliers do not match total outliers")

        # Initialise variables
        points = []
        remaining_blue, remaining_red = b, r
        centers = set()

        # Generate centers
        for i in range(num_centers):
            centers.add(self.generate_unique_point(centers))

        for center in centers:
            colour, remaining_blue, remaining_red = GraphGenerator.choose_colour(remaining_blue, remaining_red)
            if not colour:
                raise ValueError("invalid blue and red point count")
            points.append({"x": center[0], "y": center[1], "colour": colour.name.lower()})

        # Generate a single point [opt] away from each center (ensures opt is indeed the optimal solution)
        for center in centers:
            colour, remaining_blue, remaining_red = GraphGenerator.choose_colour(remaining_blue, remaining_red)
            if not colour:
                raise ValueError("invalid blue and red point count")
            edge_point = GraphGenerator.get_random_point_around_circumference(opt, center)
            points.append({"x": edge_point[0], "y": edge_point[1], "colour": colour.name.lower()})

        # Generate remaining points belonging to clusters
        for i in range(remaining_blue):
            cluster_point = GraphGenerator.get_random_point_around_circumference(opt, random.choice(tuple(centers)))
            points.append({"x": cluster_point[0], "y": cluster_point[1], "colour": Colour.BLUE.name.lower()})

        for i in range(remaining_red):
            cluster_point = GraphGenerator.get_random_point_around_circumference(opt, random.choice(tuple(centers)))
            points.append({"x": cluster_point[0], "y": cluster_point[1], "colour": Colour.RED.name.lower()})

        # Generate outlier points
        remaining_blue_outliers = np.random.randint(0, num_outliers)
        remaining_red_outliers = num_outliers - remaining_blue_outliers
        if blue_red_outliers:
            remaining_blue_outliers = blue_red_outliers[0]
            remaining_red_outliers = blue_red_outliers[1]

        for i in range(remaining_blue_outliers):
            cluster_point = self.get_random_distanced_point(opt, centers)
            points.append({"x": cluster_point[0], "y": cluster_point[1], "colour": Colour.BLUE.name.lower()})

        for i in range(remaining_red_outliers):
            cluster_point = self.get_random_distanced_point(opt, centers)
            points.append({"x": cluster_point[0], "y": cluster_point[1], "colour": Colour.RED.name.lower()})

        total_blue_points = b + remaining_blue_outliers
        total_red_points = r + remaining_red_outliers
        graph = {
            "data": points,
            "k": num_centers,
            "minBlue": b,
            "minRed": r,
            "blue": total_blue_points,
            "red": total_red_points,
            "nodes": total_blue_points + total_red_points
        }
        return graph


gen = GraphGenerator(min_x=0, min_y=0, max_x=100, max_y=100)
b = 10
r = 10
k = 4
opt = 5.5
print(gen.generate(b, r, k, opt, 5))
