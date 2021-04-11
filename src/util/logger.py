import os
import time
from collections import namedtuple
from datetime import date
from typing import Optional, List

LogEntry = namedtuple("LogEntry", ["time", "cost"])


def timestamp():
    today = str(date.today()).replace("-", "_")
    time_elapsed_today = str(int(time.time()) % 86400)
    return today + "_" + time_elapsed_today

def log_filename(name: str, n: int, k:int):
    return f"{name}_n{n}_k{k}"


class Logger:
    def __init__(self, name: str, n: int, k: int, start_time: Optional[float] = None):
        self.logs: List[LogEntry] = []
        self.name = name
        self.n = n
        self.k = k
        self.start_time = start_time or time.time()

    def append(self, cost: float):
        current_time = time.time()
        self.logs.append(LogEntry(time=current_time - self.start_time, cost=cost))

    def dump(self):
        with open(f"{log_filename(self.name, self.n, self.k)}_{timestamp()}.txt", "w") as f:
            str_logs = [f"{entry.cost} {entry.time}\n" for entry in self.logs]
            f.writelines(str_logs)
