def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part 
        # stopping once numbers[i] in correct position
        while j > 0 and numbers[j] < numbers[j - 1]:
            # Swap numbers[j] and numbers[j - 1]
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            j = j - 1


numbers = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()
 
insertion_sort(numbers)
print('SORTED:', end=' ')
for num in numbers:
    print(num, end=' ')
print()