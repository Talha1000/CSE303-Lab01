def evenOddSum(a, n):
    even = odd = 0
    for i in range(n):
        if i % 2 == 0:
            odd += a[i]
        else:
            even += a[i]
    print("Sum of even-indexed : ",even)
    print("Sum of odd-indexed : ",odd)
arr = [1,2,3,4,5,6]
n = len(arr)
evenOddSum(arr, n)