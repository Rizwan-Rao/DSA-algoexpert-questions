
# def validatesubsequence(array,subsequence):
#     arridx=0                         #these variables are used as pointers in the arrays
#     seqidx=0
#     while arridx < len(array) and seqidx < len(subsequence):
#         if array[arridx] == subsequence[seqidx]:
#             seqidx+=1
#         arridx+=1
#     return seqidx==len(subsequence)


def validatesubsequence(array, subsequence):
    seqidx=0
    for value in array:
        if seqidx==len(subsequence):
            break
        if subsequence[seqidx]==value:
            seqidx+=1
    return seqidx==len(subsequence)    

print(validatesubsequence([1,2,3,4,5,6,7,8,9,0],[2,6,9,0]))