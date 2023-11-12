# "--->-><-><-->-"
def answer(route):
    current_right_soldiers = 0
    salutes = 0
    for pos in route:
        if pos == ">":
            current_right_soldiers += 1
        if pos == "<":
            salutes += current_right_soldiers * 2
    return salutes


