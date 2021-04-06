import math
from collections import namedtuple
from pathlib import Path

InstanceConfig = namedtuple("InstanceConfig", ["nodes", "count", "k_values"])


def build_gowalla_data_set():
    locations = dict()

    gowalla_checkins_full = Path("loc-gowalla_totalCheckins.txt", "r")
    if not gowalla_checkins_full.is_file():
        print("The original Gowalla dataset is too large to upload to git, it can be downloaded at \
        https://snap.stanford.edu/data/loc-gowalla.html")

    with open("loc-gowalla_totalCheckins.txt", "r") as f:
        for line in f.readlines():
            line = line.strip().split("\t")
            latitude = line[2]
            longitude = line[3]
            loc_id = int(line[4])

            if loc_id in locations:
                locations[loc_id]["count"] += 1
            else:
                locations[loc_id] = dict()
                locations[loc_id]["latitude"] = latitude
                locations[loc_id]["longitude"] = longitude
                locations[loc_id]["count"] = 1

    with open("gowalla_checkins.txt", "w") as f:
        for loc_id in sorted(locations.keys()):
            lat = locations[loc_id]["latitude"]
            lon = locations[loc_id]["longitude"]
            count = locations[loc_id]["count"]

            f.write(f"{loc_id} {lat} {lon} {count}\n")


def divide_data_set():
    queue = [
        InstanceConfig(nodes=100, count=5, k_values=[5, 10, 10, 20, 33]),
        InstanceConfig(nodes=200, count=5, k_values=[5, 10, 20, 40, 67]),
        InstanceConfig(nodes=300, count=5, k_values=[5, 10, 30, 60, 100]),
        InstanceConfig(nodes=400, count=5, k_values=[5, 10, 28, 80, 133]),
        InstanceConfig(nodes=500, count=5, k_values=[5, 10, 50, 100, 167]),
        InstanceConfig(nodes=600, count=5, k_values=[5, 10, 60, 120, 200]),
        InstanceConfig(nodes=700, count=4, k_values=[5, 10, 70, 140]),
        InstanceConfig(nodes=800, count=3, k_values=[5, 10, 8]),
        InstanceConfig(nodes=900, count=3, k_values=[5, 10, 90])
    ]

    gowalla_checkins = Path("gowalla_checkins.txt", "r")
    if not gowalla_checkins.is_file():
        build_gowalla_data_set()

    with open("gowalla_checkins.txt", "r") as f:
        iteration = 1
        for instance in queue:
            for i in range(instance.count):
                file_name = f"gow_{iteration}.txt"
                with open(file_name) as file:
                    file.write(f"{instance.nodes} {instance.k_values[i]}\n")
                    checkins = []
                    for j in range(instance.nodes):
                        line = f.readline().strip().split(" ")
                        loc_id = line[0]
                        latitude = line[1]
                        longitude = line[2]
                        num_checkins = line[3]
                        checkins.append(int(num_checkins))
                        file.write(f"{loc_id} {latitude} {longitude} {num_checkins}\n")

                mean_checkins = sum(checkins) / len(checkins)
                above_avg = [x for x in checkins if x > mean_checkins]
                below_avg = [x for x in checkins if x <= mean_checkins]

                COVERAGE_RATIO = 0.75
                num_blue = len(above_avg)
                num_red = len(below_avg)
                min_blue = math.floor(num_blue * COVERAGE_RATIO)
                min_red = math.floor(num_red * COVERAGE_RATIO)

                header = f"{instance.count} {num_blue} {num_red} {instance.k_values[i]} {mean_checkins} {min_blue} {min_red}\n"
                with open(file_name, 'r') as original:
                    data = original.read()
                with open(file_name, 'w') as modified:
                    modified.write(header + data)


if __name__ == "__main__":
    divide_data_set()
