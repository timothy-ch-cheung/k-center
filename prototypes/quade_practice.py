import rpy2.rlike.container as rlc
import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages

# utils = rpackages.importr('utils')
# utils.chooseCRANmirror(ind=1)
# utils.install_packages(robjects.StrVector(["PMCMRplus"]))

data = robjects.IntVector([
    5, 4, 1,
    2, 3, 4,
    16, 15, 1,
    5, 6, 7,
    10, 9, 1,
    19, 18, 1,
    10, 8, 6])
problem_instances = robjects.StrVector(["pmed01", "pmed02", "pmed03", "pmed04", "pmed05", "pmed06", "pmed07"])
algorithms = robjects.StrVector(["A", "B", "C"])
dimension_names = rlc.TaggedList([problem_instances, algorithms], tags=["Problem", "Algorithm"])

data_frame = robjects.r['matrix'](data, nrow=7, byrow=True, dimnames=dimension_names)

quade_test = robjects.r["quade.test"]
result = quade_test(data_frame)
print(result)

PMCMR = rpackages.importr('PMCMRplus')

post_hoc_quade_test = quade_test = robjects.r["quadeAllPairsTest"]

result = post_hoc_quade_test(data_frame, dist="TDist", p_adjust_method="holm")

print(result)