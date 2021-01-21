import sys
def kthLargestElement1(arr, k):
    arr.sort(reverse = True)
    return arr[k - 1]

def kthLargestElement2(arr, l, r, k): 
    
    if (k > 0 and k <= r - l + 1): 
        pos = partition(arr, l, r) 
        print(pos)
        if (pos - l == k - 1): 
            return arr[pos] 
        if (pos - l > k - 1): 
            return kthLargestElement2(arr, l, pos - 1, k) 
        return kthLargestElement2(arr, pos + 1, r, k - pos + l - 1) 
  
    return sys.maxsize
  
def partition(arr, l, r): 
  
    x = arr[r] 
    i = l 
    for j in range(l, r): 
        if (arr[j] >= x): 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
    arr[i], arr[r] = arr[r], arr[i] 
    return i 
  


# arr1 = [32, 72, 40, 53, 95, 69, 3, 71, 51, 90]
# print(kthLargestElement1(arr, 3))
# print(arr)

# arr2 = [32, 72, 40, 53, 95, 69, 3, 71, 51, 90]
arr3 = [5,4,2,1,3]
print(kthLargestElement2(arr3, 0,  len(arr3) - 1, 2))
print(arr3)