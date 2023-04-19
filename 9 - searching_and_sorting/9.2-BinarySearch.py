def binary_search(numbers, key):
    low = 0
    high = len(numbers) - 1

    while high >= low:
        mid = (high + low) // 2
        if numbers[mid] < key:
            low = mid + 1
        elif numbers[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1 # not found
   

if __name__ == "__main__":
    numbers = [2, 4, 7, 10, 11, 32, 45, 87]
    print('NUMBERS:', end=' ')
    for num in numbers:
        print(num, end=' ')
    print()
    
    key = int(input('Enter a value: '))
    key_index = binary_search(numbers, key)

    if key_index == -1:
        print(f'{key} was not found.')
    else:
        print(f'Found {key} at index {key_index}.')

