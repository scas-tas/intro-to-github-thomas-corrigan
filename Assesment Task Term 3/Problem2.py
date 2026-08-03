# classroom = [["𖨆", "𖨆", "0"], # 0
#              ["0", "𖨆", "0"], # 1
#              ["0", "𖨆", "0"]] # 2

# Test Cases for count_empty

# classroom=[[1,2],[3,4]] # Test case 1
# classroom=[[1,2,0],[0,3,4],[5,0,0]] # Test case 1
# classroom=[[0,0],[0,0]] # Test case 1


# Test Cases for most_empty_row
# classroom=[[1,2,0],[0,3,4],[5,0,0]] # Test case 1
# classroom=[[1,2,3],[0,0,4],[5,0,0]] # Test case 1 
# classroom=[[1,2],[3,4]] # Test case 1



def count_empty(classroom: list) -> int:
    empty = 0
    for row in classroom:
        for seat in row:
            if seat == 0:
                empty += 1
    
    
    return empty

def most_empty_row(classroom: list) -> int:
    best_row = 0
    best_count = -1

    for row_index in range(len(classroom)):
        empty_count = 0
        for seat in classroom[row_index]:
            if seat == 0:
                empty_count += 1

        if empty_count > best_count:
            best_count = empty_count
            best_row = row_index

    return best_row

print(f"Empty Seats: {count_empty(classroom)}")
print(f"Most Empty Row: {most_empty_row(classroom)}")
for class1 in classroom:
    print(class1)