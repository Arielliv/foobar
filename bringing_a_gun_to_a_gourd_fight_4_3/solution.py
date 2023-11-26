import math


def get_all_reflected_points(point, room_dimensions, max_distance):
    mirrored_points = []
    for i in range(len(point)):
        mirrored_coordinates = []
        for j in range(-(max_distance // room_dimensions[i]) - 1, (max_distance // room_dimensions[i] + 2)):
            mirrored_coordinates.append(get_reflected_coordinate(j, point[i], room_dimensions[i]))
        mirrored_points.append(mirrored_coordinates)
    return mirrored_points


def get_reflected_coordinate(mirror, coordinate, dimension_size):
    result = coordinate
    mirror_rotation = [2 * coordinate, 2 * (dimension_size - coordinate)]

    if mirror < 0:
        for i in range(mirror, 0):
            result -= mirror_rotation[(i + 1) % 2]
    else:
        for i in range(mirror, 0, -1):
            result += mirror_rotation[i % 2]

    return result


def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def answer(room_dimensions, your_position, guard_position, max_distance):
    mirrored_points = [
        get_all_reflected_points(your_position, room_dimensions, max_distance),
        get_all_reflected_points(guard_position, room_dimensions, max_distance)
    ]

    unique_angles = set()
    angles_distances = {}

    for i in range(len(mirrored_points)):
        for j in mirrored_points[i][0]:
            for k in mirrored_points[i][1]:
                angle = math.atan2((your_position[1] - k), (your_position[0] - j))
                distance = calculate_distance(your_position, [j, k])

                if [j, k] != your_position and max_distance >= distance:
                    if (angle not in angles_distances) or (angles_distances[angle] > distance):
                        if i == 0:
                            angles_distances[angle] = distance
                        else:
                            angles_distances[angle] = distance
                            unique_angles.add(angle)

    return len(unique_angles)
