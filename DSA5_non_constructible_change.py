def nonconstructiblechange(coins):

    coins.sort()
    currentchangecreated=0

    for coin in coins:
        if coin > currentchangecreated+1:
            return currentchangecreated+1

        currentchangecreated+=coin

    return currentchangecreated+1        


coins=[5,7,1,1,2,3,22]
change=nonconstructiblechange(coins)
print(change)