def parcels(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * parcels(n - 1)

i = int(input("Enter the number: "))
result = parcels(i)
print("The possible ways to arrange the parcels is", result)