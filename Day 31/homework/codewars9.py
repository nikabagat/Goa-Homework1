def find_smallest_int(arr):
    lil_num = arr[0]
    for i in arr:
        if i < lil_num:
            lil_num = i
    return lil_num