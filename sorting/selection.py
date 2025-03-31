num = [6, 3, 5, 2, 8]

def selection(num):
    for i in range(len(num)):
        min_index = i
        for j in range(i+1, len(num)):
            if num[j] < num[min_index]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]

print(num)
selection(num)
print(num)