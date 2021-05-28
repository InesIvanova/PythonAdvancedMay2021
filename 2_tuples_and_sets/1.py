nums = tuple([float(el) for el in input().split()])

result = {}

for num in nums:
    if num not in result:
        result[num] = 0
    result[num] += 1

sorted_result = sorted(result.items(), key=lambda x: -x[1])
for key, value in sorted_result:
    print(f"{key} - {value} times")
