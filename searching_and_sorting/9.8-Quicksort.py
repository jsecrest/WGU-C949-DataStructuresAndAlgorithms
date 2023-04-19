# O(N log N)
# Recursive sort
# Partitions the list in to halves and sorts each half, recursively repeating.


def partition(numbers, i, k):
    # Pick the number at the midpoint to be the pivot value
    midpoint_index = i + (k - i) // 2
    pivot_value = numbers[midpoint_index]

    # Initialize variables
    done = False
    low_index = i
    high_index = k

    """Determine if the list is sorted. If not, swap values on the high side of
    the partition with the values on the low side of the partition"""
    while not done:
        """Search from the lower index for the first index of a value higher
        (or equal to) than the pivot value"""
        while numbers[low_index] < pivot_value:
            low_index += 1
        """Search from the higher index for the last index of a value lower 
        than the pivot value"""
        while pivot_value < numbers[high_index]:
            high_index -= 1
        """ If the values found are the same or pass each other, then there are 
        zero or one items remaining in the unsorted list. All numbers are partitioned. 
        Return high_index. """
        if low_index >= high_index:
            done = True
        else:
            """Swap numbers[low_index] and numbers[high_index],
            update low_index and high_index"""
            temp = numbers[low_index]
            numbers[low_index] = numbers[high_index]
            numbers[high_index] = temp
            low_index = low_index + 1
            high_index = high_index - 1
    return high_index


def quicksort(numbers, i, k):
    print("entering quicksort")
    j = 0
    """  Base case: If there are one or zero entries to sort,
          partition is already sorted  """
    if i >= k:
        return
    """  Partition the data within the array. Value j returned
          from partitioning is location of last item in low partition. """
    j = partition(numbers, i, k)
    """  Recursively sort low partition (i to j) and
          high partition (j + 1 to k) """
    quicksort(numbers, i, j)
    quicksort(numbers, j + 1, k)
    return


numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print("UNSORTED:", end=" ")
for num in numbers:
    print(num, end=" ")
print()

#  Initial call to quicksort
quicksort(numbers, 0, len(numbers) - 1)
print("SORTED:", end=" ")
for num in numbers:
    print(num, end=" ")
print()
