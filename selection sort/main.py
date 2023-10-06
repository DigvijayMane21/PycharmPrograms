def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = []
size=int(input("Enter the number of elements you want: "))
for e in range(size):
    ele=int(input("Enter the element: "))
    data.append(ele)

selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)