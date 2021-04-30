import sys


def parse_args():
    args = sys.argv
    INTERVAL = float(args[1])
    TIMEOUT = float(args[2])
    GRAPH_NAME = args[3]
    return INTERVAL, TIMEOUT, GRAPH_NAME
