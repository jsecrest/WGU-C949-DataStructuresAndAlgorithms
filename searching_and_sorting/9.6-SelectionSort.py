# The outcome of each outer loop (performed sequentially on each index location in the list)
# - The smallest item in the list is selected by remembering it's index in index_smallest
# - The smallest item in the list is swapped with the item at the current index
# Min run time when N is len(numbers) is N-1
# O value is O(N^2) - as a generic reference this means that the run time increases exponetially to the power of two as N increases.

# This is considered to be easy to write code by an inefficient runtime that doesn't scale well.


def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j

        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp


numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print("UNSORTED:", end=" ")
for num in numbers:
    print(num, end=" ")
print()

selection_sort(numbers)
print("SORTED:", end=" ")
for num in numbers:
    print(num, end=" ")
print()
