# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr


'''
Insertion sort:
Conceptualize a sorted half and an unsorted half 
Initially the sorted half consists of just the first element 
Iterate along the rest of the array 
Place it in its appropriate spot in the sorted half 
The sorted half grows until it encompasses the whole array 

'''
class Book:
    def __init__(self, title, author, genre):
        self.title=title
        self.author=author
        self.genre = genre

def insertion_sort_books(arr):
    #sort by title
    for i in range(1, len(arr)): #start at 1st mindexed item to have somethin to compare to to be sorted
        curr_book=arr[i]
        j = i
        #put current  book in corect spot in sorted half of arr
        #loop through sorted half and find right spot
        while j > 0 and curr_book.title < arr[j-1].title: #compares current element against element before it (j-1 would be element before it)
            #take book at j-1 and copy it to j spot
            arr[j] = arr[j-1]
            j-=1 
            #insert book at correct position
        arr[j] = curr_book

    return arr

'''PYTHON SWAP SYNTAX VERSION ^^^
    def insertion_sort_books(arr):
        for i in range(1, len(arr)):
            curr_book = arr[i]
            j=i

            while j > 0 and curr_book.title < arr[j-1].title:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1

    return arr

'''