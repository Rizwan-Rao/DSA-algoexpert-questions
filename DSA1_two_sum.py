def twonumsum(array,targetsum):
  array.sort()
  left=0
  right=len(array)-1
  while left<right:
    currentsum = array[left]+array[right]
    if currentsum==targetsum:
      return[array[left],array[right]]
    elif currentsum<targetsum:
      left+=1
    elif currentsum >targetsum:
      right-=1
  return[]    

print(twonumsum([2,5,6,7,4,8,1,-7],10))