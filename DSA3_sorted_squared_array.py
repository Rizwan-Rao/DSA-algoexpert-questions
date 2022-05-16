# def sortedsquaredarray(array):
#     sortedSquares = [0 for _ in array]          #way to make array of zeroes
    
#     for i in range(len(array)):
#         value = array[i]
#         sortedSquares[i]= value*value
#     sortedSquares.sort()
#     return sortedSquares



def sortedsquaredarray(array):
    sortedSquares = [0 for _ in array]
    smallervalueidx = 0
    largervalueidx = len(array)-1 

    for i in reversed(range(len(array))):
        smallervalue = array[smallervalueidx]
        largervalue = array[largervalueidx]

        if abs(smallervalue)>abs(largervalue):
            sortedSquares[i] = smallervalue*smallervalue
            smallervalueidx+=1
        else:
            sortedSquares[i]= largervalue*largervalue
            largervalueidx-=1
    return sortedSquares



print(sortedsquaredarray([-5,-4,-2,1,2,3,4,5,6,7,8,9]))