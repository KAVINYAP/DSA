class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None

  # 1. Create linked list
  def create_list(self):
    n = int(input("Enter the number of nodes to create: "))
    for i in range(n):
      data = int(input(f"Enter data for node {i + 1}: "))
      self.insert_at_end(data)
    print("Linked list created successfully!")

  # 2. Insert at beginning
  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
    print(f"Inserted {data} at the beginning.")

  # 3. Insert at end
  def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  # 4. Insert at specific index (0-based index)
  def insert_at_index(self, index, data):
    if index < 0:
      print("Invalid index!")
      return
    if index == 0:
      self.insert_at_beginning(data)
      return

    new_node = Node(data)
    current = self.head
    count = 0
    while current and count < index - 1:
      current = current.next
      count += 1

    if not current:
      print("Index out of bounds!")
      return

    new_node.next = current.next
    current.next = new_node
    print(f"Inserted {data} at index {index}.")

  # 5. Delete by value
  def delete_by_value(self, data):
    if not self.head:
      print("Linked list is empty!")
      return

    if self.head.data == data:
      self.head = self.head.next
      print(f"Node with value {data} deleted.")
      return

    current = self.head
    while current.next and current.next.data != data:
      current = current.next

    if not current.next:
      print(f"Value {data} not found in the linked list.")
    else:
      current.next = current.next.next
      print(f"Node with value {data} deleted.")

  # 6. Delete first node
  def delete_first(self):
    if not self.head:
      print("Linked list is empty!")
      return
    deleted_data = self.head.data
    self.head = self.head.next
    print(f"Deleted first node with value: {deleted_data}")

  # 7. Delete last node
  def delete_last(self):
    if not self.head:
      print("Linked list is empty!")
      return

    if not self.head.next:
      deleted_data = self.head.data
      self.head = None
      print(f"Deleted last node with value: {deleted_data}")
      return

    current = self.head
    while current.next.next:
      current = current.next

    deleted_data = current.next.data
    current.next = None
    print(f"Deleted last node with value: {deleted_data}")

  # 8. Count number of nodes
  def count_nodes(self):
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count

  # 9. Display / Traverse
  def display(self):
    if not self.head:
      print("Linked list is empty!")
      return
    current = self.head
    elements = []
    while current:
      elements.append(str(current.data))
      current = current.next
    print(" -> ".join(elements) + " -> None")


# --- Main Menu Driver Program ---
if __name__ == "__main__":
  ll = LinkedList()

  while True:
    print("\n--- Singly Linked List Menu ---")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Specific Index")
    print("5. Delete by Value")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    if choice == "1":
      ll.create_list()
    elif choice == "2":
      val = int(input("Enter value to insert at beginning: "))
      ll.insert_at_beginning(val)
    elif choice == "3":
      val = int(input("Enter value to insert at end: "))
      ll.insert_at_end(val)
      print(f"Inserted {val} at the end.")
    elif choice == "4":
      idx = int(input("Enter index (0-based): "))
      val = int(input("Enter value to insert: "))
      ll.insert_at_index(idx, val)
    elif choice == "5":
      val = int(input("Enter value to delete: "))
      ll.delete_by_value(val)
    elif choice == "6":
      ll.delete_first()
    elif choice == "7":
      ll.delete_last()
    elif choice == "8":
      print(f"Total number of nodes: {ll.count_nodes()}")
    elif choice == "9":
      print("Linked List: ", end="")
      ll.display()
    elif choice == "10":
      print("Exiting program. Goodbye!")
      break
    else:
      print("Invalid choice! Please enter a number between 1 and 10.")
