from typing import List


def binarySearch(myList: List[int], item: int) -> bool:
    first = 0
    end = len(myList) - 1
    found = False
    while not found and first <= end:
        mid = (first + end) // 2
        if myList[mid] == item:
            found == True
        else:
            if item < myList[mid]:
                end = mid
            else:
                first = mid + 1
    return found