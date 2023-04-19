## Selection Sort

### Overview
Find(select) the smallest number in the unsorted part of the list and compare it with the value of the index in the current sorted part. Then swap it into the current index.

### Algorithm
1. Selection sort treats the input as two parts, sorted and unsorted. Variables i and j keep track of the two parts.
2. The selection sort algorithm searches the unsorted part of the array for the smallest element. Index_smallest stores the index of the smallest element found.
3. Elements at i and index_smallest are swapped.
4. Indices for the sorted and unsorted parts are updated.
5. The unsorted part is searched again, swapping the smallest element with the element at i.
6. The process repeats until all elements are sorted.

## Insertion Sort

### Overview
The first element of the list is counted as sorted. Check the next element of the list to see if it's less than the last element of the sorted list. If so, swap the two values. Then repeat with previous elements of the list until the value is inserted into it's correctly sorted location.

### Algorithm
1. Selection sort treats the input as two parts, sorted and unsorted. Variables i and j keep track of the two parts.
2. The selection sort algorithm searches the unsorted part of the array for the smallest element. Index_smallest stores the index of the smallest element found.
3. Elements at i and index_smallest are swapped.
4. Indices for the sorted and unsorted parts are updated.
5. The unsorted part is searched again, swapping the smallest element with the element at i.
6. The process repeats until all elements are sorted.