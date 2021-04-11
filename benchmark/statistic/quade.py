import math
from typing import List, Tuple

import rpy2.rlike.container as rlc
import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages


def validate_data(algorithm_labels: List[str], problem_labels: List[str], measurements: Tuple[List[float]]):
    if len(algorithm_labels) != len(measurements):
        raise ValueError("Number of measurement sets must equal the number of algorithms")
    for measurement in measurements:
        if len(measurement) != len(problem_labels):
            raise ValueError("Number of measurements per set must equal the number of problem instances/trials")


def package_data(algorithm_labels: List[str], problem_labels: List[str], measurements: Tuple[List[float]]):
    validate_data(algorithm_labels, problem_labels, measurements
                  )
    data = robjects.IntVector([val for pair in zip(*measurements) for val in pair])
    problem_instances = robjects.StrVector(problem_labels)
    algorithms = robjects.StrVector(algorithm_labels)
    dimension_names = rlc.TaggedList([problem_instances, algorithms], tags=["Problem", "Algorithm"])
    data_frame = robjects.r['matrix'](data, nrow=len(problem_labels), byrow=True, dimnames=dimension_names)

    return data_frame


def quade_test(algorithm_labels: List[str], problem_labels: List[str], measurements: Tuple[List[float]]):
    data_frame = package_data(algorithm_labels, problem_labels, measurements)

    quade_test = robjects.r["quade.test"]
    result = quade_test(data_frame)
    p_value = result.rx2("p.value")[0]
    return p_value


def post_hoc_quade_test(algorithm_labels: List[str], problem_labels: List[str], measurements: Tuple[List[float]]):
    data_frame = package_data(algorithm_labels, problem_labels, measurements)

    rpackages.importr('PMCMRplus')
    post_hoc_quade_test = robjects.r["quadeAllPairsTest"]
    result = post_hoc_quade_test(data_frame, dist="TDist", p_adjust_method="holm")

    p_values = dict()
    columns = list(result.rx2("p.value").colnames)
    rows = list(result.rx2("p.value").rownames)
    for col in columns:
        for row in rows:
            p_value = result.rx2("p.value").rx(row, col)[0]
            if not math.isnan(p_value):
                p_values[(col, row)] = p_value

    return p_values
