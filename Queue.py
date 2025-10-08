class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear: 
            self.front = self.rear = new_node
            print(f"Enqueued {data} to queue")
            print("Time Complexity: O(1), Space Complexity: O(1)")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data} to queue")
        print("Time Complexity: O(1), Space Complexity: O(1)")

    def dequeue(self):
        if not self.front:
            print("Queue is empty. Cannot dequeue.")
            return
        removed = self.front.data
        self.front = self.front.next
        if not self.front: 
            self.rear = None
        print(f"Dequeued {removed} from queue")
        print("Time Complexity: O(1), Space Complexity: O(1)")

    def peek(self):
        if not self.front:
            print("Queue is empty.")
            return
        print(f"Front element is: {self.front.data}")
        print("Time Complexity: O(1), Space Complexity: O(1)")

    def display(self):
        if not self.front:
            print("Queue is empty.")
            return
        current = self.front
        print("Queue from front to rear:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")
        print("Time Complexity: O(n), Space Complexity: O(1)")


queue = Queue()

while True:
    print("\nChoose an option:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value to enqueue: "))
        queue.enqueue(val)

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
        print("Invalid choice! Try again.")
