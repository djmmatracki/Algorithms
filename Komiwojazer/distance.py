
def distance_points(first, second):
    return abs(first - second)

def distance_tour(aTour):
    return sum(distance_points(aTour[i-1], aTour[i]) for i in range(len(aTour)))