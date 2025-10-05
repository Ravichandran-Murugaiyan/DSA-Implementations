
n = int(input("Enter the number of elements: "))

array = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

print("\nOriginal array:", array)

swap_count = 0  # Track swaps for performance detection

# Selection Sort
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if array[j] < array[min_index]:
            min_index = j
    if min_index != i:
        # Swap the elements
        array[i], array[min_index] = array[min_index], array[i]
        swap_count += 1

# Determine performance case
if swap_count == 0:
    performance = "Best Case (Already Sorted)"
elif swap_count < n // 2:
    performance = "Average Case (Partially Sorted)"
else:
    performance = "Worst Case (Reverse Sorted or Nearly Reverse)"

# Display results
print("\nSorted array:", array)
print(f"Performance Case: {performance}")


print("\nSpace Complexity:")
print("  O(1) - In-place sorting (no extra space except few variables)")
