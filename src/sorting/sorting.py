# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
   elements = len(arrA) + len(arrB)
   merged_arr =[0] * elements
   x=0
   for i in arrA:
       for j in arrB:
           if i<j:
               merged_arr[x]=i
               x+=1
           else:
               merged_arr[x]=j
               x+=1
    
    
    


   return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        piv = len(arr) // 2
        left = arr[:piv]
        right = arr[piv:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    return arr

def merge_sort_in_place(arr, l, r):
    # Your code here
    return arr
