from typing import List

def insertionSort(myList: List[int]):
    for i in range(1, len(myList)):
        element_next = myList[i]
        j = i - 1
        while j >= 0 and myList[j] > element_next:
            myList[j+1] = myList[j]
            j -= 1
        myList[j+1] = element_next
    return myList

