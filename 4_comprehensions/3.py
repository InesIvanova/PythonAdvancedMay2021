n = int(input())

matrix = [[int(el) for el in input().split(", ") if int(el) % 2 == 0]
          for _ in range(n)]

# Here we iter one more time which is not necessary,
# but if we do not filter above it will be
# matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
# even_matrix = [[num for num in sublist if num % 2 == 0] for sublist in matrix]
print(matrix)