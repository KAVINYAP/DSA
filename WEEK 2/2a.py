n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")

for i in range(n):
    element = int(input())
    arr.append(element)

key = int(input("Enter the element to search: "))

found = False

for i in range(n):
    if arr[i] == key:
        print("Element found at position", i + 1)
        found = True
        break

if not found:
    print("Element not found")
