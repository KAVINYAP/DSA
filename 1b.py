p = float(input("Enter the principal growth factor"))
n = int(input("Enter the number of years"))
def calculate(p,n):
    if n==1:
        return p
    else:
        return p * calculate(p,n-1)
print(calculate(p,n))