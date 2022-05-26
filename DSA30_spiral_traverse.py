# # First method
# def spiraltraversal(array):
#     result=[]
#     startrow,endrow=0,len(array)-1
#     startcol,endcol=0,len(array[0])-1

#     while startrow<=endrow and startcol<=endcol:

#         for col in range(startcol,endcol+1):
#             result.append(array[startrow][col])

#         for row in range(startrow+1,endrow+1):
#             result.append(array[row][endcol])

#         for col in reversed(range(startcol,endcol)):
#             result.append(array[endrow][col])

#         for row in reversed(range(startrow+1,endrow)):
#             result.append(array[row][startcol]) 

#         startrow+=1
#         endrow-=1 
#         startcol+=1 
#         endcol-=1 
#     return result


# Second method


def spiraltraversal(array):
    
    result=[]
    spiralfill(array,0,len(array)-1,0,len(array[0])-1,result)
    return result

def spiralfill(array,startrow,endrow,startcol,endcol,result):

    if startrow>endrow and startcol>endcol:
        return
    
    for col in range(startcol,endcol+1):
        result.append(array[startrow][col])

    for row in range(startrow+1,endrow+1):
        result.append(array[row][endcol])

    for col in reversed(range(startcol,endcol)):
        result.append(array[endrow][col])

    for row in reversed(range(startrow+1,endrow)):
        result.append(array[row][startcol]) 

    spiralfill(array,startrow+1,endrow-1,startcol+1,endcol-1,result)


array=[[1,2,3],[4,5,6],[7,8,9]]     
print(spiraltraversal(array))             