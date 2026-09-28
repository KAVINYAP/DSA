1. class Queue:

    def __init__(self):
        self.queue = []
        self.max_size = 5

    # ENQUEUE
    def enqueue(self, data):

        if len(self.queue) == self.max_size:
            print("Overflow! Queue is full.")
            return

        self.queue.append(data)
        print(f"Enqueued '{data}' into the queue.")

    # DEQUEUE
    def dequeue(self):

        if len(self.queue) == 0:
            print("Underflow! Queue is empty.")
            return None

        removed_data = self.queue.pop(0)
        print(f"Dequeued '{removed_data}' from the queue.")
        return removed_data

    # PEEK
    def peek(self):

        if len(self.queue) == 0:
            print("Queue is empty.")
            return None

        print(f"Front element is: {self.queue[0]}")
        return self.queue[0]

    # DISPLAY
    def display(self):

        if len(self.queue) == 0:
            print("Queue is empty.")
            return

        print("Queue elements (front to rear):")

        for item in self.queue:
            print(f"| {item} |", end=" ")

        print()


# Menu-driven program

my_queue = Queue()

while True:

    print("\n--- Queue Using Array ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':

        item = input("Enter the value to enqueue: ")
        my_queue.enqueue(item)

    elif choice == '2':

        my_queue.dequeue()

    elif choice == '3':

        my_queue.peek()

    elif choice == '4':

        my_queue.display()

    elif choice == '5':

        print("Exiting program. Goodbye!")
        break

    else:

        print("Invalid choice! Please enter a number between 1 and 5.")

2. class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # ENQUEUE
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(f"Enqueued '{data}' into the queue.")

    # DEQUEUE
    def dequeue(self):
        if self.front is None:
            print("Underflow! Queue is empty.")
            return None

        removed_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"Dequeued '{removed_data}' from the queue.")
        return removed_data

    # PEEK
    def peek(self):
        if self.front is None:
            print("Queue is empty.")
            return None

        print(f"Front element is: {self.front.data}")
        return self.front.data

    # DISPLAY
    def display(self):
        if self.front is None:
            print("Queue is empty.")
            return

        print("Queue elements (front to rear):")
        current = self.front

        while current is not None:
            print(f"| {current.data} |", end=" ")
            current = current.next

        print()

# Menu-driven program
my_queue = Queue()

while True:
    print("\n--- Queue Using Linked List ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        item = input("Enter the value to enqueue: ")
        my_queue.enqueue(item)

    elif choice == '2':
        my_queue.dequeue()

    elif choice == '3':
        my_queue.peek()

    elif choice == '4':
        my_queue.display()

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
