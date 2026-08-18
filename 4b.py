def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

# User input
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

arr = quick_sort(arr)

print("Sorted array:")
for element in arr:
    print(element, end=" ")