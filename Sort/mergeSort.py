from typing import List


def mergeSort(myList: List[int]) -> None:
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0 # left
        j = 0 # right

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
                k += 1
            else:
                myList[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1

mylist = [32, 2, 1, 7, 87, 9]

mergeSort(mylist)
print(mylist)