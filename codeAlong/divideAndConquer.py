#Sum numbers in an array

def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

print(sum([1, 2, 3, 4]))

#Count the amount of elements in an array

def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

print(count([1, 2, 3, 4]))

#Find the biggest number in an array

def findMax(arr):
    if arr == []:
        return 0
    if arr[0] > findMax(arr[1:]):
        return arr[0]
    return findMax(arr[1:])

print(findMax([10, 2, 15, 6, 35]))