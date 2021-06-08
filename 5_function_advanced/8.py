def expression(nums, current_result=0, current_expression=""):
    if not nums:
        print(f"{current_expression}={current_result}")
        return
    expression(nums[1:], current_result+nums[0], f'{current_expression}+{nums[0]}')
    expression(nums[1:], current_result-nums[0], f'{current_expression}-{nums[0]}')

result = 0
for i in range(5):
    result =+1

nums = [int(el) for el in input().split(", ")]
expression(nums)
