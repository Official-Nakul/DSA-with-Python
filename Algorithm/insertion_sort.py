def insertion_sort(num):
    for i in range(0, len(num) - 1):
        for j in range(i + 1, 0, -1):  # loop will run reverse, from current index to 0
            if num[j] < num[j - 1]:
                num[j], num[j - 1] = num[j - 1], num[j]
            else:
                break


num = [0, 3, 5, 6, 2, 1, 4, 7, 8, 9]

insertion_sort(num)

print(num)
