from ArrayList import *
from sortingTechnique import *

def Driver(array,technique):
    print("The unsorted Array is: ", array)

    if technique == "INSERTION":
        print("The sorted Array with Insertion sort is: ", insertionSort(array))
    elif technique == "BUBBLE":
        print("The sorted Array with Bubble sort  is: ", bubbleSort(array))
    elif technique == "MERGE":
        print("The sorted Array with Merge sort is: ", mergeSort(array))
    elif technique == "SELECTION":
        print("The sorted Array with Selection sort is: ", selectionSort(array))
    elif technique == "QUICK":
        print("The sorted Array with Quick sort is: ", quickSort(0, len(array) - 1, array))
    elif technique == "HEAP":
        print("The sorted Array with Heap sort is: ", heapSort(array))
    else:
        print("Wrong arguments")
    
if __name__ == "__main__":
    Driver(array1,"INSERTION")
    Driver(array2,"INSERTION")
    Driver(array3,"INSERTION")
    print("\n")
    Driver(array1,"BUBBLE")
    Driver(array2,"BUBBLE")
    Driver(array3,"BUBBLE")
    print("\n")
    Driver(array1,"MERGE")
    Driver(array2,"MERGE")
    Driver(array3,"MERGE")
    print("\n")
    Driver(array1,"SELECTION")
    Driver(array2,"SELECTION")
    Driver(array3,"SELECTION")
    print("\n")
    Driver(array1,"QUICK")
    Driver(array2,"QUICK")
    Driver(array3,"QUICK")
    print("\n")
    Driver(array1,"HEAP")
    Driver(array2,"HEAP")
    Driver(array3,"HEAP")