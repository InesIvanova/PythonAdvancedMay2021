n = int(input())

cars = set()

for _ in range(n):
   command, number = input().split(", ")

   if command == "IN":
       cars.add(number)
   else:
       cars.discard(number)

if not cars:
    print("Parking Lot is Empty")
else:
    [print(car) for car in cars]

