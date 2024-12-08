import numpy as np

def parse_input(filename):
    with open(filename, 'r') as f:
        content = f.read().strip().split('\n')
    return np.array([list(line) for line in content])

def locate_all_antennas(antennas_map):
    antennas_locations = {}
    for i in range(antennas_map.shape[0]):
        for j in range(antennas_map.shape[1]):
            antenna_type = antennas_map[i, j]
            if antenna_type != '.':
                antennas_locations[antenna_type] = antennas_locations.get(antenna_type, []) + [(i, j)]
    return antennas_locations

def distance_from_antenna(map_point, antenna_location):
    return np.array([
        antenna_location[0] - map_point[0],
        antenna_location[1] - map_point[1]
    ])

def antennas_pair_radiate_at_point(antenna, pairing_antenna, point):
    d1 = distance_from_antenna(antenna, pairing_antenna)
    d2 = distance_from_antenna(point, antenna)
    for k in range(MAX_RANGE):
        if ((k*d1 - d2) == 0).all():
            return True
    return False


def antennas_radiate_at_point(antennas_locations, point):
    for i in range(len(antennas_locations)-1):
        antenna = antennas_locations[i]
        for j in range(i+1, len(antennas_locations)):
            pairing_antenna = antennas_locations[j]
            if antennas_pair_radiate_at_point(
                antenna, pairing_antenna, point
            ) or antennas_pair_radiate_at_point(
                pairing_antenna, antenna, point
            ):
                return True
    return False
            


antennas_map = parse_input('input.txt')
antennas_locations = locate_all_antennas(antennas_map)
MAX_RANGE = max(antennas_map.shape) + 1
radiations_map = np.full(antennas_map.shape, '.')


for i in range(antennas_map.shape[0]):
    for j in range(antennas_map.shape[1]):
        for antenna_type in antennas_locations:
            if antennas_radiate_at_point(
                antennas_locations=antennas_locations[antenna_type],
                point=(i, j)
            ):
                radiations_map[i, j] = "#"
print((radiations_map == '#').sum())
for i in range(antennas_map.shape[0]):
    for j in range(antennas_map.shape[1]):
        if antennas_map[i, j] != '.':
            radiations_map[i, j] = antennas_map[i, j]
# print(radiations_map)
