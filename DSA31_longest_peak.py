def longestpeak(array):

    longestpeaklength=0
    i=1
    while i < len(array)-1:

        ispeak= array[i-1]<array[i] and array[i]>array[i+1]

        if not ispeak:
            i+=1
            continue

        leftidx=i-2
        while leftidx>=0 and array[leftidx]<array[leftidx-1]:
            leftidx-=1
        rightidx=i+2 
        while rightidx<len(array) and array[rightidx]<array[rightidx-1]:
            rightidx+=1 

        currentpeaklength= rightidx-leftidx-1 
        longestpeaklength= max(longestpeaklength,currentpeaklength) 
        i= rightidx
        
    return longestpeaklength      


array=[1,2,3,3,4,0,10,6,5,-1,-3,2,3]
print(longestpeak(array))    