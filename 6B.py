class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top is None

    def push(self, data):
        """Add an element to the top of the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed '{data}' into the stack.")

    def pop(self):
        """Remove and return the top element from the stack."""
        if self.is_empty():
            print("\nUnderflow! Stack is empty.")
            return None
        popped_node = self.top
        self.top = self.top.next
        print(f"Popped '{popped_node.data}' from the stack.")
        return popped_node.data

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("\nStack is empty.")
            return None
        print(f"Top element is: {self.top.data}")
        return self.top.data

    def display(self):
        """Display all elements in the stack from top to bottom."""
        if self.is_empty():
            print("\nStack is empty.")
        else:
            print("\nStack elements (top to bottom):")
            current = self.top
            while current:
                print(f"| {current.data} |")
                current = current.next
            print("-------")

# Interactive Menu
my_stack = Stack()

while True:
    print("\n--- Linked List Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        item = input("Enter the value to push: ")
        my_stack.push(item)
    elif choice == '2':
        my_stack.pop()
    elif choice == '3':
        my_stack.peek()
    elif choice == '4':
        my_stack.display()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")