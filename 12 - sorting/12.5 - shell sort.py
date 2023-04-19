# shell sort works by doing lots of small sorts to reduce the work of a final large sort
# it works by creating several interleaved lists
# (we don't make new lists, they exist as interleaved lists within the original list)
# we perform insertion sort on each list independently of each other (inside the original list)
# this mini sort brings lower values closer to the front so that eventually doing an insertion
# the entire list is more efficient.

# gap = the number of lists to create. 
# In cases like 3 lists for a 7 element list, the lists will vary in size

# example
# [2,5,4,3,1] with gap=3
# 3 lists will be sorted: 
# The first element of each list is chosen as the first three elements [2,]  [5,]  [4]
# the second element comes from the second three elements              [2,3] [5,1] [4]
# Sort the lists in place in the original list. In this case only the 5 and 1 swap places
# The sorted lists look like [2,3][1,5][4]
# Because they are sorted in place in the original list the new list looks like [2,1,4,3,5]
# Then maybe we chose a gap size of 2:
# 2 lists are sorted [2,4,5] [1,3]
# Both lists are already sorted so no values swap positions [2,1,4,3,5]
# Finally we would sort with gap = 1 (only one list)
# This is the same as a normal insertion sort. Every shell sort must end with gap = 1
# The result is a fully sorted list. 


def insertion_sort_interleaved(numbers, start_index, gap):
    swaps = 0
    for i in range(start_index + gap, len(numbers), gap):
        j = i
        while (j - gap >= start_index) and (numbers[j] < numbers[j - gap]):
            swaps += 1
            temp = numbers[j]
            numbers[j] = numbers[j - gap]
            numbers[j - gap] = temp
            j = j - gap
    return swaps

          
def shell_sort(numbers, gap_values):
    swaps = []
    for gap_value in gap_values:
        for i in range(gap_value):
            swaps.append(insertion_sort_interleaved(numbers, i, gap_value))
    return swaps

                        
# Main program to test the shell sort algorithm.
numbers = [12, 18, 3, 72, 65, 22, 19]
print('UNSORTED: ', numbers)

swaps = shell_sort(numbers, [4, 2, 1])
print('SORTED: ', numbers)
print('Total swaps:', swaps)
