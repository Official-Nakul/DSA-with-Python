def divide(num, left, right):
    if left < right:
        mid = left+(right-left)//2
        divide(num, left, mid)
        divide(num, mid+1, right)
        merge(num, left, mid, right)


def merge(num, left, mid, right):
    i = left
    j = mid+1
    temp = []
    while i <= mid and j <= right:
        if num[i] > num[j]:
            temp.append(num[j])
            j += 1

        else:
            temp.append(num[i])
            i += 1
    while i <= mid:
        temp.append(num[i])
        i += 1
    while j <= right:
        temp.append(num[j])
        j += 1
    for i in range(0, len(temp)):
        num[left+i] = temp[i]


num = [4, 6, 0, 1, 2, 3, 7, 8, 9, 5, -1, -3, -4]
divide(num, 0, len(num)-1)
print(num)
