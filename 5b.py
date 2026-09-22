class Node:

  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None


class DoublyLinkedList:

  def __init__(self):
    self.head = None

  # 1. Create linked list
  def create_list(self):
    n = int(input("Enter the number of nodes to create: "))
    for i in range(n):
      data = int(input(f"Enter data for node {i + 1}: "))
      self.insert_at_end(data)
    print("Doubly linked list created successfully!")

  # 2. Insert at beginning
  def insert_at_beginning(self, data):
    new_node = Node(data)
    if self.head is not None:
      new_node.next = self.head
      self.head.prev = new_node
    self.head = new_node
    print(f"Inserted {data} at the beginning.")

  # 3. Insert at end
  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return

    current = self.head
    while current.next is not None:
      current = current.next

    current.next = new_node
    new_node.prev = current

  # 4. Insert at specific index (0-based index)
  def insert_at_index(self, index, data):
    if index < 0:
      print("Invalid index!")
      return
    if index == 0:
      self.insert_at_beginning(data)
      return

    current = self.head
    count = 0
    while current is not None and count < index - 1:
      current = current.next
      count += 1

    if current is None:
      print("Index out of bounds!")
      return

    new_node = Node(data)
    new_node.next = current.next
    new_node.prev = current

    if current.next is not None:
      current.next.prev = new_node
    current.next = new_node
    print(f"Inserted {data} at index {index}.")

  # 5. Delete by value
  def delete_by_value(self, data):
    if self.head is None:
      print("Linked list is empty!")
      return

    current = self.head

    # If the node to delete is the head
    if current.data == data:
      self.delete_first()
      return

    while current is not None and current.data != data:
      current = current.next

    if current is None:
      print(f"Value {data} not found in the linked list.")
      return

    # If it's an intermediate or last node
    if current.next is not None:
      current.next.prev = current.prev
    if current.prev is not None:
      current.prev.next = current.next

    print(f"Node with value {data} deleted.")

  # 6. Delete first node
  def delete_first(self):
    if self.head is None:
      print("Linked list is empty!")
      return

    deleted_data = self.head.data
    if self.head.next is not None:
      self.head = self.head.next
      self.head.prev = None
    else:
      self.head = None

    print(f"Deleted first node with value: {deleted_data}")

  # 7. Delete last node
  def delete_last(self):
    if self.head is None:
      print("Linked list is empty!")
      return

    current = self.head
    if current.next is None:
      deleted_data = current.data
      self.head = None
      print(f"Deleted last node with value: {deleted_data}")
      return

    while current.next is not None:
      current = current.next

    deleted_data = current.data
    current.prev.next = None
    print(f"Deleted last node with value: {deleted_data}")

  # 8. Count number of nodes
  def count_nodes(self):
    count = 0
    current = self.head
    while current is not None:
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
    while current is not None:
      elements.append(str(current.data))
      current = current.next
    print(" <-> ".join(elements) + " <-> None")


# --- Main Menu Driver Program ---
if __name__ == "__main__":
  dll = DoublyLinkedList()

  while True:
    print("\n--- Doubly Linked List Menu ---")
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
      dll.create_list()
    elif choice == "2":
      val = int(input("Enter value to insert at beginning: "))
      dll.insert_at_beginning(val)
    elif choice == "3":
      val = int(input("Enter value to insert at end: "))
      dll.insert_at_end(val)
      print(f"Inserted {val} at the end.")
    elif choice == "4":
      idx = int(input("Enter index (0-based): "))
      val = int(input("Enter value to insert: "))
      dll.insert_at_index(idx, val)
    elif choice == "5":
      val = int(input("Enter value to delete: "))
      dll.delete_by_value(val)
    elif choice == "6":
      dll.delete_first()
    elif choice == "7":
      dll.delete_last()
    elif choice == "8":
      print(f"Total number of nodes: {dll.count_nodes()}")
    elif choice == "9":
      print("Doubly Linked List: ", end="")
      dll.display()
    elif choice == "10":
      print("Exiting program. Goodbye!")
      break
    else:
      print("Invalid choice! Please enter a number between 1 and 10.")