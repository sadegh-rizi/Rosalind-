with open("rosalind_hea.txt") as f:
    n=int(f.readline())
    arr=[int(x) for x in f.readline().split(" ")]

def heapify_down(arr,i):
    n= len(arr)
    first_parent = int((n-2)/2)# another -1 because index of the last child is n-1

    if i>first_parent: # Stop at leaf
       return None
    else:
    
        left = 2*i+1
        right= 2*i+2
        # print(f"i,left,right:{i,left,right}")
        if right==n:  # If the first parent doesn't have a right child, this condition is checked to account for index error
            j=left
        else:
            if arr[left]>=arr[right]:
                j= left
            else:
                j= right
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            heapify_down(arr,j)
def build_heap(arr):
    n=len(arr)
    first_parent = int((n-2)/2)

    for i in range(first_parent,-1,-1):
        heapify_down(arr,i)
    return arr
with open("output.txt",'w') as f:
    f.write(" ".join([str(x) for x in build_heap(arr)]))
