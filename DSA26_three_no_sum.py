def threenumbersum(array,targetsum):
    array.sort()
    triplets=[]

    for i in range(len(array)-2):
        left=i+1
        right=len(array)-1
        while left<right:
            currentsum= array[i]+array[left]+array[right]
            if currentsum == targetsum:
                triplets.append([array[i],array[left],array[right]])
                left+=1
                right-=1
            elif currentsum<targetsum:
                left+=1
            elif currentsum>targetsum:
                right-=1        
    return triplets


print(threenumbersum([-8,-6,1,2,3,5,6,12],0))                