
# Hashing Implementation

SIZE = 10

# Separate Chaining
class SeparateChaining:
    def __init__(self):
        self.table = [[] for _ in range(SIZE)]

    def insert(self, key):
        index = key % SIZE
        if key not in self.table[index]:
            self.table[index].append(key)

    def display(self):
        print("Separate Chaining:")
        for i in range(SIZE):
            print(i, ":", self.table[i])


# Linear Probing
class LinearProbing:
    def __init__(self):
        self.table = [None] * SIZE

    def insert(self, key):
        index = key % SIZE
        for i in range(SIZE):
            new_index = (index + i) % SIZE
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
        print("Hash Table is Full!")

    def display(self):
        print("Linear Probing:")
        for i in range(SIZE):
            print(i, ":", self.table[i])


# Quadratic Probing
class QuadraticProbing:
    def __init__(self):
        self.table = [None] * SIZE

    def insert(self, key):
        index = key % SIZE
        for i in range(SIZE):
            new_index = (index + i * i) % SIZE
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
        print("Hash Table is Full!")

    def display(self):
        print("Quadratic Probing:")
        for i in range(SIZE):
            print(i, ":", self.table[i])


# Main Program
sc = SeparateChaining()
lp = LinearProbing()
qp = QuadraticProbing()

while True:
    print("\n1. Insert")
    print("2. Display Separate Chaining")
    print("3. Display Linear Probing")
    print("4. Display Quadratic Probing")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        sc.insert(key)
        lp.insert(key)
        qp.insert(key)

    elif choice == 2:
        sc.display()

    elif choice == 3:
        lp.display()

    elif choice == 4:
        qp.display()

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
