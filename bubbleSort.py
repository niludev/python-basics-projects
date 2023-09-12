def bubble_sort(arr):
    n = len(arr)
    print(n)
    for i in range(n):
        print('i:', i)
        
        swapped = False
        for j in range(0, n-i-1):
            print('range:', range(0, n-i-1))
            print('j:',j,'arr[j]:',arr[j],'j+1:',j+1,'arr[j+1]:', arr[j+1])

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break
        
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("sorted list:", sorted_arr)

for i in range(0,7):
    print(i)