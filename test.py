def is_increasing(arr):
    
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False

    return True


print(is_increasing([5, 3, 7, 101]))