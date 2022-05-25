def smallestDifference(arrayOne,arrayTwo):

    arrayOne.sort()
    arrayTwo.sort()
    idxone = 0
    idxtwo = 0
    current= float("inf")
    smallest= float("inf")
    smallestpair=[]

    while idxone<len(arrayOne) and idxtwo<len(arraytwo):

        firstnum = arrayOne[idxone]
        secondnum =arrayTwo[idxtwo]

        if firstnum <secondnum:
            current = secondnum - firstnum
            idxone+=1
        elif secondnum<firstnum:
            current = firstnum - secondnum
            idxtwo+=1
        else:
            return [firstnum,secondnum]

        if current<smallest:
            smallest=current
            smallestpair=[firstnum,secondnum]
    return smallestpair           


arrayone=[5,8,25,69,54,21,12,32,17,18,19,32,25]
arraytwo=[51,81,75,45,63,95,45,71,42,41,9]
print(smallestDifference(arrayone,arraytwo))     