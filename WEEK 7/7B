class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.rear = None

    # ENQUEUE operation
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            # First node points to itself
            self.rear = new_node
            new_node.next = new_node
        else:
            # Insert after rear and make new node the rear
            new_node.next = self.rear.next
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into the queue.")

    # DEQUEUE operation
    def dequeue(self):
        if self.rear is None:
            print("Queue is empty.")
        else:
            front = self.rear.next

            if front == self.rear:
                # Only one node
                self.rear = None
            else:
                self.rear.next = front.next

            print(front.data, "deleted from the queue.")

    # PEEK operation
    def peek(self):
        if self.rear is None:
            print("Queue is empty.")
        else:
            print("Front element:", self.rear.next.data)

    # DISPLAY operation
    def display(self):
        if self.rear is None:
            print("Queue is empty.")
        else:
            print("Queue elements are:", end=" ")

            front = self.rear.next
            temp = front

            while True:
                print(temp.data, end=" ")
                temp = temp.next

                if temp == front:
                    break

            print()

# Menu-driven program
queue = CircularQueue()

while True:
    print("\n--- QUEUE MENU ---")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter the element to enqueue: "))
        queue.enqueue(data)

    elif choice == 2:
        queue.dequeue()

    elif choice == 3:
        queue.peek()

    elif choice == 4:
        queue.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")

