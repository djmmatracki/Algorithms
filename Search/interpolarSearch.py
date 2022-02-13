from typing import List

def intSearch(myList: List[int], x: int) -> bool:
    idx0 = 0
    idxn = len(myList) - 1
    found = False
    while idx0 <= idxn and x >= myList[idx0] and x <= myList[idxn]:
        mid = idx0 + int(((float(idxn - idx0) / (myList[idxn] - myList[idx0])) * (x - myList[idx0])))

        if myList[mid] == x:
            found = True