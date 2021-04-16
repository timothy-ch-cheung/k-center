from typing import List

import rpy2.robjects as robjects


def wilcoxon_test(measurements_x: List[float], measurements_y: List[float]) -> float:
    """Perform a Wilcoxon signed rank test"""
    wilcoxon = robjects.r["wilcox.test"]
    x = robjects.FloatVector(measurements_x)
    y = robjects.FloatVector(measurements_y)
    result = wilcoxon(x, y, paired=True)
    p_value = result.rx2("p.value")[0]
    return p_value
