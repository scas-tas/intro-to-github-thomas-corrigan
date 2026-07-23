def count_empty(classroom: list) -> int:
    count = 0
    for row in classroom:
        # TODO: loop through each seat in this row and update count
        pass
    return count
 
def most_empty_row(classroom: list) -> int:
    best_row = 0
    best_count = -1
    for row_index in range(len(classroom)):
        # TODO: count the empty seats in classroom[row_index]
        # TODO: if this row has more empty seats than best_count,
        #       update best_row and best_count
        pass
    return best_row
