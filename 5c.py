class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class CircularLinkedList:

  def __init__(self):
    self.head = None

  # 1. Create linked list
  def create_list(self):
    n = int(input("Enter the number of nodes to create: "))
    for i in range(n):
      data = int(input(f"Enter data for node {i + 1}: "))
      self.insert_at_end(data)
    print("Circular linked list created successfully!")

  # 2. Insert at beginning
  def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      new_node.next = self.head
    else:
      current = self.head
      while current.next != self.head:
        current = current.next
      current.next = new_node
      new_node.next = self.head
      self.head = new_node
    print(f"Inserted {data} at the beginning.")

  # 3. Insert at end
  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      new_node.next = self.head
    else:
      current = self.head
      while current.next != self.head:
        current = current.next
      current.next = new_node
      new_node.next = self.head

  # 4. Insert at specific index (0-based index)
  def insert_at_index(self, index, data):
    total_nodes = self.count_nodes()
    if index < 0 or index > total_nodes:
      print("Index out of bounds!")
      return
    if index == 0:
      self.insert_at_beginning(data)
      return
    if index == total_nodes:
      self.insert_at_end(data)
      print(f"Inserted {data} at index {index}.")
      return

    current = self.head
    for _ in range(index - 1):
      current = current.next

    new_node = Node(data)
    new_node.next = current.next
    current.next = new_node
    print(f"Inserted {data} at index {index}.")

  # 5. Delete by value
  def delete_by_value(self, data):
    if self.head is None:
      print("Linked list is empty!")
      return

    current = self.head
    if current.data == data:
      self.delete_first()
      return

    prev = None
    while current.next != self.head:
      prev = current
      current = current.next
      if current.data == data:
        prev.next = current.next
        print(f"Node with value {data} deleted.")
        return

    print(f"Value {data} not found in the linked list.")

  # 6. Delete first node
  def delete_first(self):
    if self.head is None:
      print("Linked list is empty!")
      return

    deleted_data = self.head.data
    if self.head.next == self.head:
      self.head = None
    else:
      current = self.head
      while current.next != self.head:
        current = current.next
      current.next = self.head.next
      self.head = self.head.next
    print(f"Deleted first node with value: {deleted_data}")

  # 7. Delete last node
  def delete_last(self):
    if self.head is None:
      print("Linked list is empty!")
      return

    deleted_data = None
    if self.head.next == self.head:
      deleted_data = self.head.data
      self.head = None
    else:
      current = self.head
      while current.next.next != self.head:
        current = current.next
      deleted_data = current.next.data
      current.next = self.head
    print(f"Deleted last node with value: {deleted_data}")

  # 8. Count number of nodes
  def count_nodes(self):
    if self.head is None:
      return 0
    count = 1
    current = self.head.next
    while current != self.head:
      count += 1
      current = current.next
    return count

  # 9. Display / Traverse
  def display(self):
    if self.head is None:
      print("Linked list is empty!")
      return
    current = self.head
    elements = []
    while True:
      elements.append(str(current.data))
      current = current.next
      if current == self.head:
        break
    print(" -> ".join(elements) + " -> (points back to head)")


# --- Main Menu Driver Program ---
if __name__ == "__main__":
  cll = CircularLinkedList()

  while True:
    print("\n--- Circular Linked List Menu ---")
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
      cll.create_list()
    elif choice == "2":
      val = int(input("Enter value to insert at beginning: "))
      cll.insert_at_beginning(val)
    elif choice == "3":
      val = int(input("Enter value to insert at end: "))
      cll.insert_at_end(val)
      print(f"Inserted {val} at the end.")
    elif choice == "4":
      idx = int(input("Enter index (0-based): "))
      val = int(input("Enter value to insert: "))
      cll.insert_at_index(idx, val)
    elif choice == "5":
      val = int(input("Enter value to delete: "))
      cll.delete_by_value(val)
    elif choice == "6":
      cll.delete_first()
    elif choice == "7":
      cll.delete_last()
    elif choice == "8":
      print(f"Total number of nodes: {cll.count_nodes()}")
    elif choice == "9":
      print("Circular Linked List: ", end="")
      cll.display()
    elif choice == "10":
      print("Exiting program. Goodbye!")
      break
    else:
      print("Invalid choice! Please enter a number between 1 and 10.")