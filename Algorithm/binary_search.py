def binary_search(num, i, j, target):

    left = i
    right = j
    while left <= right:
        mid = left+(right-left)//2
        if target == num[mid]:
            return mid
        elif target < num[mid]:
            right = mid-1
        else:
            left = mid+1
    return mid


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter Element you wnat to Find: "))

inx = binary_search(num, 0, len(num)-1, target)

if target == num[inx]:
    print(f"Element Found at Index {inx}")
else:
    if num[0] > target:
        print(f"Element should be Inserted at Index 0")
    else:
        print(f"Element should be Inserted at Index {inx+1}")
