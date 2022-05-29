# def arrayofproducts(array):
#     products=[1 for _ in range(len(array)) ]

#     for i in range(len(array)):
#         runningproduct=1
#         for j in range(len(array)):
#             if i!=j:
#                 runningproduct*=array[j]
#         products[i]=runningproduct 
#     return products           


# def arrayofproducts(array):
#     products=[1 for _ in range(len(array))]
#     leftproducts=[1 for _ in range(len(array))]
#     rightproducts=[1 for _ in range(len(array))]

#     leftrunningproduct=1
#     for i in range(len(array)):
#         leftproducts[i]= leftrunningproduct
#         leftrunningproduct*=array[i]

#     rightrunningproduct=1
#     for i in reversed(range(len(array))):
#         rightproducts[i]=rightrunningproduct
#         rightrunningproduct*=array[i]

#     for i in range(len(array)):
#         products[i] = leftproducts[i]* rightproducts[i]

#     return products



def arrayofproducts(array):

    products=[1 for _ in range(len(array))]

    leftrunningproduct=1
    for i in range(len(array)):
        products[i]=leftrunningproduct
        leftrunningproduct*=array[i]
    
    rightrunningproduct=1
    for i in reversed(range(len(array))):
        products[i]*=rightrunningproduct
        rightrunningproduct*=array[i]

    return products

array=[5,1,4,2]
print(arrayofproducts(array))