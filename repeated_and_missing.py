def repeatedandmissing(arr, size):
    str_rep = {}
    for i in range(len(arr)):
        val = arr[i]
        if str_rep.get(val):
            print("Repeated No: ", arr[i])
        else:
            str_rep[val] = 1
    
    for i in range(1, len(str_rep)+1):
        if i not in str_rep:
            print("Missing No: ", i)
  
# Driver program to test above function */
arr = [7, 3, 4, 5, 5, 6, 2]
n = len(arr)
repeatedandmissing(arr, n)