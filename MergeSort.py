n = int(input("Enter the number of elements: "))

array = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

print("\nOriginal array:", array)

merge_operations = 0  

def merge_sort(arr):
    global merge_operations
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            merge_operations += 1  

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            merge_operations += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            merge_operations += 1

merge_sort(array)
if merge_operations <= n * (n.bit_length()):
    performance = "Best Case (Already Sorted or Small Array)"
elif merge_operations < (n * (n.bit_length()) * 2):
    performance = "Average Case"
else:
    performance = "Worst Case (Reverse Sorted or Large Array)"

# Display results
print("\nSorted array:", array)
print(f"Performance Case: {performance}")

print("\nSpace Complexity:")
print("  O(n) - Extra space used for temporary arrays during merging")
