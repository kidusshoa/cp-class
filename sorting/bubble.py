def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n-i-1):
            if num[j] > num [j+1]:
                num[j], num[j+1] = num[j+1], num[j]

num = [3, 5, 4, 8, 2]
print(num)
bubble_sort(num)
print(num)