import sys

max_int = sys.maxsize
current_row_size = 8
current_col_size = 8


def answer(src, dest):
    result = calc_points_as_matrix(src, dest, current_row_size, current_col_size)
    start_point = result["start_point"]
    dest_point = result["dest_point"]
    been_here = {}
    return count_number_of_min_steps_to_win(start_point, dest_point, been_here)


def calc_points_as_matrix(src, dest, row_size, col_size):
    counter = 0
    for x in range(0, row_size):
        for y in range(0, col_size):
            if counter == src:
                start_point = {"x": x, "y": y}
            elif counter == dest:
                dest_point = {"x": x, "y": y}
            counter += 1
    return {"start_point": start_point, "dest_point": dest_point}


def count_number_of_min_steps_to_win(current_point, dest_point, been_here):
    key = f"{current_point['x']}-{current_point['y']}"
    if key in been_here or current_point["x"] < 0 or current_point["x"] > current_row_size - 1 or current_point["y"] < 0 or current_point[
        "y"] > current_col_size - 1:
        return max_int

    if current_point["x"] == dest_point["x"] and current_point["y"] == dest_point["y"]:
        return 0

    been_here[key] = True
    moves = [
        {"x": -2, "y": -1}, {"x": -2, "y": 1}, {"x": -1, "y": -2}, {"x": -1, "y": 2},
        {"x": 1, "y": -2}, {"x": 1, "y": 2}, {"x": 2, "y": -1}, {"x": 2, "y": 1}
    ]

    min_steps = max_int
    for move in moves:
        new_point = {"x": current_point["x"] + move["x"], "y": current_point["y"] + move["y"]}
        steps = 1 + count_number_of_min_steps_to_win(new_point, dest_point, been_here)
        min_steps = min(min_steps, steps)

    return min_steps

# -------------------------
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
# -------------------------
# | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
# -------------------------
# | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
# -------------------------
# | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
# -------------------------
# | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |
# -------------------------
# | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
# -------------------------
# | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 |
# -------------------------
# | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 |
# -------------------------
#
# -------------------------
# | 0, 0, 0 | 0, 1, 1 | 0, 2, 2 | 0, 3, 3 | 0, 4, 4 | 0, 5, 5 | 0, 6, 6 | 0, 7, 7 |
# -------------------------
# | 1, 0, 8 | 1, 1, 9 | 1, 2, 10 | 1, 3, 11 | 1, 4, 12 | 1, 5, 13 | 1, 6, 14 | 1, 7, 15 |
# -------------------------
# | 2, 0, 16 | 2, 1, 17 | 2, 2, 18 | 2, 3, 19 | 2, 4, 20 | 2, 5, 21 | 2, 6, 22 | 2, 7, 23 |
# -------------------------
# | 3, 0, 24 | 3, 1, 25 | 3, 2, 26 | 3, 3, 27 | 3, 4, 28 | 3, 5, 29 | 3, 6, 30 | 3, 7, 31 |
# -------------------------
# | 4, 0, 32 | 4, 1, 33 | 4, 2, 34 | 4, 3, 35 | 4, 4, 36 | 4, 5, 37 | 4, 6, 38 | 4, 7, 39 |
# -------------------------
# | 5, 0, 40 | 5, 1, 41 | 5, 2, 42 | 5, 3, 43 | 5, 4, 44 | 5, 5, 45 | 5, 6, 46 | 5, 7, 47 |
# -------------------------
# | 6, 0, 48 | 6, 1, 49 | 6, 2, 50 | 6, 3, 51 | 6, 4, 52 | 6, 5, 53 | 6, 6, 54 | 6, 7, 55 |
# -------------------------
# | 7, 0, 56 | 7, 1, 57 | 7, 2, 58 | 7, 3, 59 | 7, 4, 60 | 7, 5, 61 | 7, 6, 62 | 7, 7, 63 |
# -------------------------
