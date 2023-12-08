def selection_sort(num):
    for i in range(0, len(num)):
        maxInx = 0
        lastInx = len(num) - i - 1
        for j in range(1, lastInx+1):
            if num[j] > num[maxInx]:
                maxInx = j
        num[maxInx], num[lastInx] = num[lastInx], num[maxInx]


arr = [5, 8, 9, 3, 2, 1, 0, 7, 4, 6]

selection_sort(arr)

print(arr)
