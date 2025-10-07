n = int(input("Enter the number of elements: "))
shift_count=0
array = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

print("\nOriginal array:", array)

for i in range(1, n):
    key = array[i]
    j = i - 1
    shifted = False
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
        shift_count += 1
        shifted = True
    array[j + 1] = key
    if not shifted:
        shift_count += 0  

if shift_count == 0:
    performance = "Best Case (Already Sorted)"
elif shift_count < (n * (n - 1)) // 4:
    performance = "Average Case (Partially Sorted)"
else:
    performance = "Worst Case (Reverse Sorted or Nearly Reverse)"

print("\nSorted array:", array)
print(f"Performance Case: {performance}")

print("\nSpace Complexity:")
print("  O(1) - In-place sorting (no extra space except few variables)")
