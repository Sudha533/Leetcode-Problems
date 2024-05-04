def findMax(arr):
    max_number = float('-inf')
    for num in arr:
        if num > max_number:
            max_number = num
    print(max_number)
arr = [-1,-6,-9,-4,-99]
findMax(arr)