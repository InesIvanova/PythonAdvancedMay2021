word = list(input())
result = []

while word:
    result.append(word.pop())

print(f"{''.join(result)}")