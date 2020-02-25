# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr_a, arr_b):
    merged_arr = []
    # TO-DO

    # Initialize indices
    index_a = 0
    index_b = 0

    # While loop through it:

    # If both indices are within the bounds of their respective arrays
    while len(arr_a) > index_a and len(arr_b) > index_b:
        # Add to list if A is less than B and increment index_a
        if arr_a[index_a] < arr_b[index_b]:
            merged_arr.append(arr_a[index_a])
            index_a += 1
        # Otherwise, add to list and increment index_b
        else:
            merged_arr.append(arr_b[index_b])
            index_b += 1

    # Shove remainder from arr_a into merged_arr
    while len(arr_a) > index_a:
        merged_arr.append(arr_a[index_a])
        index_a += 1

    # Shove remainder from arr_b into merged_arr
    while len(arr_b) > index_b:
        merged_arr.append(arr_b[index_b])
        index_b += 1

    # Celebrate
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:

        while True:
            index_m = int(len(arr) * 0.5)
            arr_l = merge_sort(arr[:index_m])
            arr_r = merge_sort(arr[index_m:])
            return merge(arr_l, arr_r)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
