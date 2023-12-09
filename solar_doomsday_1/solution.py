def answer(area):
    result = []
    while area > 0:
        # Find the largest square that can be created
        side_length = int(area ** 0.5)
        largest_square = side_length ** 2

        # Append the largest square to the result
        result.append(largest_square)

        # Update the remaining area
        area -= largest_square

    return result
