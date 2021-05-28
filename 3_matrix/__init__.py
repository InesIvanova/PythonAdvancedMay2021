def creating_matrix_from_user_input(r):
    initial_matrix = []
    for u_input in range(r):
        user_input = [int(el) for el in input().split(", ")]
        initial_matrix.append(user_input)
    return initial_matrix


def is_sub_matrix_full(current_sub_m):
    if len(current_sub_m) == 4:
        return True
    return False


def creating_sub_matrix_from_initial_matrix(data):
    boxes = []
    start_column = 0
    start_row = 0
    while start_row < rows_count - 1:
        curr_box = []
        for row in range(2):
            if is_sub_matrix_full(curr_box):
                break
            for column in range(2):
                curr_el = data[start_row + row][start_column + column]
                curr_box.append(curr_el)
        boxes.append(curr_box)
        start_column += 1
        if start_column == len(matrix[0]) - 1:
            start_row += 1
            start_column = 0
    return boxes


def create_list_with_max_values(data):
    return [sum(el) for el in data]


def finding_first_occ_of_max_value(list1, data):
    index = list1.index(max(list1))
    return data[index]


def print_result(max_sub_matrix):
    print(
        f"{max_sub_matrix[0]} {max_sub_matrix[1]} \n{max_sub_matrix[2]} {max_sub_matrix[3]}")
    print(sum(max_sub_matrix))


rows_count, columns_count = map(int, input().split(", "))

matrix = creating_matrix_from_user_input(rows_count)

sub_matrix = creating_sub_matrix_from_initial_matrix(matrix)

sums_list = create_list_with_max_values(sub_matrix)
first_max_el_in_sub_m = finding_first_occ_of_max_value(sums_list, sub_matrix)

print_result(first_max_el_in_sub_m)