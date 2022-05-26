def isMonotonic(array):
    isnotdecreasing=True
    isnotincreasing=True
    for i in range(1,len(array)):
        if array[i]<array[i-1]:
            isnotdecreasing=False
        if array[i]>array[i-1]:
            isnotincreasing=False    
    return isnotincreasing or isnotdecreasing        

array=[-1,-5,-10,-1100,-1100,-1101,-1103,-9001]
print(isMonotonic(array))