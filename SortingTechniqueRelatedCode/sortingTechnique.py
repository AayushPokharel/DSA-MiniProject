##
# Code for Insertion Sort
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j] :
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
##

##
# Code for Bubble Sort
def bubbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    return array
##

##
# Code for Selection Sort
def selectionSort(array):
    for i in range(len(array)): # first loop runs for (n)times
        min_idx = i
        for j in range(i+1, len(array)): # second looop runs for (n-1)times
            if array[min_idx] > array[j]:   # is only executed when pair is out of order
                min_idx = j
    
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
##

##
# Code for Merge Sort
def mergeSort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

    return array
##

##
# Code for Quick Sort

#function definition of partition function
def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:                        # k is number of elements less than pivot
        while start < len(array) and array[start] <= pivot: start += 1 # this is done T(k) times
        while array[end] > pivot: end -= 1    # this is done T(n-k-1) times
        if(start < end):
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end

# main() function
def quickSort(start, end, array):
    if (start < end):
        p = partition(start, end, array)    # This partitioning gives O(n)
        quickSort(start, p - 1, array)      #   recursive call
        quickSort(p + 1, end, array)        #   recursive call
    return array
##

##
# Code for Heap Sort

#function definition of heapify function
def heapify(array, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[largest] < array[l]: largest = l
    if r < n and array[largest] < array[r]: largest = r
        
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)    

# main() function
def heapSort(array):
    n = len(array)

    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)      

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array      
##