from typing import List


Index = int

def binary_serach(myList: List[int], item: int) -> Index:
    
    start = 0
    end = len(myList) - 1
    foundFlag = False
    while not foundFlag and start <= end:
        mid = (start+end)//2
        if myList[mid] == item:
            foundFlag = True
        else:
            if myList[mid] < item:
                start = mid + 1
            else:
                end = mid - 1
    return mid
