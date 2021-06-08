# file = open("numbers.txt")
# result = 0
#
# for line in file:
#     result += int(line)
# file.close()
# print(result)



# This way we close the file automatically

# with open("numbers.txt") as file:
#     result = 0
#     for line in file:
#         result += int(line)
#     print(result)


print(sum([int(line) for line in open("numbers.txt")]))