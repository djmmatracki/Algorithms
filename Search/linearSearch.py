

def linearSearch(myList, item):
    index = 0
    found = False
    while not found and index < len(myList):
        if myList[index] == item:
            found = True
        else:
            index += 1