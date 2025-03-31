num = [4, 7, 3, 9, 3, 6]

def merge_sort(num):
    if len(num) > 1:
        mid = len(num) // 2
        L = num[:mid]
        R = num[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                num[k] = L[i]
                i += 1
            else:
                num[k] = R[j]
                j += 1
            k +=1
            
        while i < len(L):
            num[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
             num[k] = R[j]
             j += 1
             k += 1

print(num)
merge_sort(num)
print(num)