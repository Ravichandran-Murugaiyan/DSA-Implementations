
n = int(input("Enter the number of elements: "))

array = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

print("\nOriginal array:", array)

swap_count = 0 

# Bubble Sort (Sorting the elements)
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            swapped = True
            swap_count += 1 # calculates the swap count to calculate the complexity
    if not swapped:
        break 
# Determine performance case
if swap_count == 0:
    performance = "Best Case (Already Sorted)"
elif swap_count < (n * (n - 1)) // 4:
    performance = "Average Case (Partially Sorted)"
else:
    performance = "Worst Case (Reverse Sorted or Nearly Reverse)"

# Display results
print("\nSorted array:", array)
print(f"Performance Case: {performance}")

print("\nSpace Complexity:")
print("  O(1) - In-place sorting (no extra space except few variables)")
