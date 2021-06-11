from advanced_modules.math_operations.constants import operation_mapper

num_1, operator, num_2 = input().split()

num_1 = float(num_1)
num_2 = float(num_2)

print(operation_mapper[operator](num_1, num_2) if operation_mapper.get(operator) else "Invalid operator")
