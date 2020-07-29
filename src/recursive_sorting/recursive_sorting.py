# TO-DO: complete the helper function below to merge 2 sorted arrays.
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    i = 0  #will point to arrA(first_half)
    j = 0  #will point to arrB(second_half)

    # TO-DO
    for index in range(0, elements):
        # if arrA[i] < arrB[j]:
        if i >= len(arrA):
            merged_arr[index] = arrB[j]
            j += 1
        elif j >= len(arrB):
            merged_arr[index] = arrA[i]
            i += 1
        elif arrA[i] < arrB[j]:
            merged_arr[index] = arrA[i]
            i += 1
        else:
            merged_arr[index] = arrB[j]
            j += 1


    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    #base case
    if len(arr) > 1:
        #split the array
        length = len(arr)
        middle = length // 2
        
        
        first_half = merge_sort(arr[:middle])
        second_half = merge_sort(arr[middle:])
            
                      
        #merge left and right sorted arrays
        arr = merge(first_half,second_half)
    

    return arr



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
