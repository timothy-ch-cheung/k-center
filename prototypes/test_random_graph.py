from prototypes.random_graph import GraphGenerator
import numpy as np


def test_get_random_point_around_circumference():
    point = (0, 0)
    target_distance = 5
    generated_point = GraphGenerator.get_random_point_around_circumference(target_distance, point)
    assert np.linalg.norm(np.array(point) - np.array(generated_point)) == 5
