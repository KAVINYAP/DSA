class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def push(self, item):
        """Add an element to the top of the stack."""
        self.stack.append(item)
        print(f"Pushed '{item}' into the stack.")

    def pop(self):
        """Remove and return the top element from the stack."""
        if self.is_empty():
            print("\nUnderflow! Stack is empty.")
            return None
        removed_item = self.stack.pop()
        print(f"Popped '{removed_item}' from the stack.")
        return removed_item

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            print("\nStack is empty.")
            return None
        print(f"Top element is: {self.stack[-1]}")

    def display(self):
        """Display all elements in the stack."""
        if self.is_empty():
            print("\nStack is empty.")
        else:
            print("\nStack elements (top to bottom):")
            for item in reversed(self.stack):
                print(f"| {item} |")
            print("-------")

# Interactive Menu
my_stack = Stack()

while True:
    print("\n--- Stack Operations Menu ---")
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
