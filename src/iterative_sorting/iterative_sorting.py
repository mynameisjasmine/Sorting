# TO-DO: Complete the selection_sort() function below. 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        #(hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
             if arr[j] < arr[smallest_index]:
                smallest_index = j        

        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
             
        #TO-DO: swap
        
         
        # arr[cur_index] = arr[smallest_index]
        # arr[smallest_index] = arr[cur_index]
        
    return arr


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

# print('Check:', selection_sort(arr1)) 

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
       for i in range(0, len(arr)-1):
           curr_index = i
           smaller_index = curr_index

           for j in range(curr_index, len(arr)):
               if arr[j] < arr[curr_index] :
                
                   arr[j], arr[smaller_index] = arr[smaller_index], arr[j]
               
                    # continue
                


     
       return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print('Checking bubble', bubble_sort(arr1))


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

#     return arr




