class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} to stack")
        print("Time Complexity: O(1), Space Complexity: O(1)")

    def pop(self):
        if not self.top:
            print("Stack is empty. Cannot pop.")
            return
        popped = self.top.data
        self.top = self.top.next
        print(f"Popped {popped} from stack")
        print("Time Complexity: O(1), Space Complexity: O(1)")

    def peek(self):
        if not self.top:
            print("Stack is empty.")
            return
        print(f"Top element is: {self.top.data}")
        print("Time Complexity: O(1), Space Complexity: O(1)")

    def display(self):
        if not self.top:
            print("Stack is empty.")
            return
        current = self.top
        print("Stack from top to bottom:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")
        print("Time Complexity: O(n), Space Complexity: O(1)")

stack = Stack()

while True:
    print("\nChoose an option:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value to push: "))
        stack.push(val)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.peek()

    elif choice == 4:
        stack.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
