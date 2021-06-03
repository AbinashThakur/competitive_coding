def get_element(value,low, high, key):
    mid = 0
    
    if high < low:
        return -1

    mid = (low + high) // 2
    
    if value[mid] == key:
        return mid

    if value[mid] >= value[low]:
        if key >= value[low] and key <= value[mid]:
            return get_element(value, low, mid-1, key)
        return get_element(value, mid+1, high, key)
        
    if key >= value[mid] and key <= value[high]:
        return get_element(value, low, mid+1, key)
    return get_element(value, low, mid-1, key)


x = [3,4,5,1,2]
y = 4
n = len(x)
print(get_element(x,0, n-1, y))