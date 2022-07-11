#ćwiczenia 

#1

numbers = [number for number in range (1, 21)]
print(numbers)

#2 
#for number in range(1, 1000000):
#    print(number)

#3

million = list(range(1, 1000001))

print(max(million),'\n')
print(min(million), '\n')
print(sum(million))

#4
odds = list(range(1, 21, 2))
print(odds)

#5
triplet = list(range(3, 32, 3))

for three in triplet:
    print(three)

#6 i 7
cubes = [number**3 for number in range(1, 11)]

for number in cubes:
    print(number)