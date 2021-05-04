import sys

import click

from benchmark.tools.benchmark.benchmark_gowalla import run_gowalla_suite
from benchmark.tools.benchmark.benchmark_orlib import run_orlib_suite
from benchmark.tools.benchmark.benchmark_synthetic import run_synthetic_suite

ALGORITHM_MAP = {
    "gon": "greedy",
    "grasp_ps": "grasp_ps",
    "pbs": "target_pbs",
    "ban": "colourful_bandyapadhyay",
    "col_pbs": "target_colourful_pbs"
}

DATA_SETS = {"ORLIB", "GOWALLA", "SYNTHETIC"}

def valid(data_set, algorithm):
    valid = True
    if data_set not in DATA_SETS:
        print("Invalid DATA_SET, run 'python cli.py info' for valid arguments")
        valid = False

    if algorithm not in ALGORITHM_MAP:
        print("Invalid ALGORITHM, run 'python cli.py info' for valid arguments")
        valid = False

    return valid


@click.group()
def main():
    pass


@main.command()
def info():
    """Print valid argument options"""
    print("Valid data sets: ['ORLIB', 'GOWALLA', 'SYNTHETIC']")
    print("Valid algorithms: ['gon', 'grasp_ps', 'pbs', 'ban', 'col_pbs']")


@main.command()
@click.argument('data_set')
@click.argument('algorithm')
@click.option("--trials", "-tr", default=1, help='Number of trials')
@click.option("--timeout", "-to", default=-1, help='Timeout (seconds) for each trial')
def benchmark(data_set, algorithm, trials, timeout):
    """Benchmark ALGORITHM on DATA_SET"""
    benchmark_handler = {
        "GOWALLA": run_gowalla_suite,
        "SYNTHETIC": run_synthetic_suite,
        "ORLIB": run_orlib_suite
    }

    if not valid(data_set, algorithm):
        return

    algorithm = ALGORITHM_MAP[algorithm]
    print(f"Benchmarking {algorithm} on {data_set} for {trials} {'trial' if trials == 1 else 'trials'}")
    benchmark_handler[data_set](algorithm, trials, timeout)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(['--help'])
    else:
        main()
