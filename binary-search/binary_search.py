def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")
    start = 0
    end = len(search_list) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if value < search_list[mid]:
            end = mid - 1
        elif value > search_list[mid]:
            start = mid+1
        else:
            return mid
    return 0
            
