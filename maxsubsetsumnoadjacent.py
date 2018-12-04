def maxsums(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    
    maxsums = arr[:]
    maxsums[1] = max(arr[0], arr[1])
    for i in range 2(len(arr)):
        maxsums[i] = max(maxsums[i - 1], maxsums[i-2] + arr[i])
    return maxsums[-1]



    