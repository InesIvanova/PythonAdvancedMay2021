# numbers_list = [int(el) for el in input().split(", ")]
# result = 1
#
# for number in numbers_list:
#     if number <= 5:
#         result *= number
#     elif number > 5:
#         result /= number
#
# print(result)
from custom_dir.helpers import sum_nums

print(sum_nums(6, 7))
