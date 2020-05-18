def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search(returns index of target, if exissts in array, otherwise returns -1(meaning not in arr))
#assume arr is sorted
def binary_search(arr, target):
    #figure out total size of arr
    left = 0
    right = len(arr)-1 #will get entire length of array then divide to get midpoint
     #most;ly when left doesnt start with 0
    while left <= right:
        #find midpoint
        mid = (left + right) //2
        #check if midpoibnt = target
        if arr[mid] ==target:
            return mid
        #check to see if element should be on left or right of midpoint
        if arr[mid] <target:
            #toss out the left side, target is on right
            #update left index
            left = mid + 1
        #if midpoint is greater than:
        else:
            #toss out right side, target on left
            right = mid -1
    # not found
    return -1  
