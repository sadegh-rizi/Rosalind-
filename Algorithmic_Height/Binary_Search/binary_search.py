def recur_binary_search(array,k,low,high):
    # base case:


    if high>=low:
        mid = (high+low)//2
        if k==array[mid]:
            return mid+1
        elif k>array[mid]:
            return recur_binary_search(array,k,mid+1,high)

        elif k<array[mid]:
            return recur_binary_search(array,k,low,mid-1)

    else:
        return -1   

def iter_binary_search(array,k):
    high=len(array)-1
    low=0
    while high-low>=0:
        mid = (high+low)//2
        if k>array[mid]:
            low=mid+1
        elif k< array[mid]:
            high=mid-1
        else:
            return mid+1 
        
    return -1


        
with open("rosalind_bins.txt") as f:
    n=int(f.readline())
    m=int(f.readline())
    array=[int(x) for x in f.readline().split(" ")]
    ks=[int(x) for x in f.readline().split(" ")]
with open('output.txt','w') as f:
    f.write(" ".join([str(recur_binary_search(array,k,0,n)) for k in ks ]))
