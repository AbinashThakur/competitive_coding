def subarrysum(arr, n ,sum):
    cur_sum = arr[0]
    start = 0
    
    i = 1
    while i<=n:
        
        while cur_sum > sum and start < i-1:
            cur_sum = cur_sum - arr[start]
            start += 1
        
        if cur_sum == sum:
            print(start, i-1)
            return 1
        
        if i < n:
            cur_sum = cur_sum + arr[i]
        i += 1
        
    print("No subarry found")
    return 0

ar = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(ar)
sum = 23
subarrysum(ar, n, sum)