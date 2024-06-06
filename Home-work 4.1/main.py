def move_zeros_to_end(lst):

    non_zero_elements = [x for x in lst if x != 0]

    zero_count = lst.count(0)

    return non_zero_elements + [0] * zero_count


print(move_zeros_to_end([0, 1, 0, 12, 3]))  # [1, 12, 3, 0, 0]
print(move_zeros_to_end([0]))               # [0]
print(move_zeros_to_end([1, 0, 13, 0, 0, 0, 5]))  # [1, 13, 5, 0, 0, 0, 0]
print(move_zeros_to_end([9, 0, 7, 31, 0, 45, 0, 45, 0, 96, 0]))  # [9, 7, 31, 45, 45, 96, 0, 0, 0, 0, 0]
