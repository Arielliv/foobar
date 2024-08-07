from collections import deque


def solution(src, dest):
    if src == dest:
        return 0

    knight_possible_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    start = convert_linear_coordinate_into_2d_coordinate(src)
    end = convert_linear_coordinate_into_2d_coordinate(dest)

    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        current_pos, depth = queue.popleft()

        for move in knight_possible_moves:
            new_pos = (current_pos[0] + move[0], current_pos[1] + move[1])

            if 0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 8 and new_pos not in visited:
                if new_pos == end:
                    return depth + 1
                queue.append((new_pos, depth + 1))
                visited.add(new_pos)

    return None


def convert_linear_coordinate_into_2d_coordinate(coordinate):
    coordinate_2d = (coordinate // 8, coordinate % 8)
    return coordinate_2d
