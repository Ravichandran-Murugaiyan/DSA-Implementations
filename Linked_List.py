class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List():
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            print("Time Complexity: O(1), Space Complexity: O(1)")
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        print("Time Complexity: O(n), Space Complexity: O(1)")

    def display(self):
        if not self.head:
            print("There is no values in the Linked List !!")
            return
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("Null")
        print("Time Complexity: O(n), Space Complexity: O(1)")

    def delete(self,data):
        if not self.head:
            print("There is no Element to Delete !!")
            return
        current=self.head
        if current and current.data == data:
            self.head=current.next
            print("Time Complexity: O(1), Space Complexity: O(1)")
            return
        prev=None
        while current and current.data!=data:
            prev=current
            current=current.next
        if current:
            prev.next=current.next
            print("Time Complexity: O(n), Space Complexity: O(1)")
        else:
            print("Element not found to delete !!")

    def search(self, data):
        current = self.head
        pos = 0
        while current:
            if current.data == data:
                print(f"Element {data} found at position {pos}")
                print("Time Complexity: O(n), Space Complexity: O(1)")
                return
            current = current.next
            pos += 1
        print(f"Element {data} not found in the list !!")
        print("Time Complexity: O(n), Space Complexity: O(1)")


# ---------------- Menu Driven Program ----------------
Linked_List = Linked_List()

while True:
    print("\nChoose an option:")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value to insert: "))
        Linked_List.append(val)

    elif choice == 2:
        val = int(input("Enter value to delete: "))
        Linked_List.delete(val)

    elif choice == 3:
        val = int(input("Enter value to search: "))
        Linked_List.search(val)

    elif choice == 4:
        Linked_List.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
