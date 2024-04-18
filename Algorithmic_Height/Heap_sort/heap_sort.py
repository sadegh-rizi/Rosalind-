with open("rosalind_hs.txt") as f:
    n=int(f.readline())
    arr=[int(x) for x in f.readline().split(" ")]
#arr= [1,3,5,7,2]
def heapify_down(arr,n,i):
    #n= len(arr)
    first_parent = int((n-2)/2)# another -1 because index of the last child is n-1
    
    if i>first_parent: # Stop at leaf
       return None
    else:
        
        left = 2*i+1
        right= 2*i+2
        # print(f"i,left,right:{i,left,right}")
        if right==n:
            return None
        j=i
        if left<n and arr[left]>=arr[right]:
            j= left
        elif right<n and arr[left]<arr[right]:
            j= right
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
            heapify_down(arr,n,j)
def build_heap(arr):
    n=len(arr)
    first_parent = int((n-2)/2)

    for i in range(first_parent,-1,-1):
        heapify_down(arr,n,i)
    return arr

def heap_sort(arr):
    heap = build_heap(arr)
    end= len(arr)-1
    while end>1:
        #print(end)
        heap[0],heap[end]=heap[end],heap[0]
        #print(f"heap before sifting down:{heap}")

        heapify_down(heap,end,0)
        #print(f"heap after sifting down:{heap}")

        end= end-1
    return heap
with open("output.txt",'w') as f:
    f.write(" ".join([str(x) for x in heap_sort(arr)]))
#print(heap_sort(arr))
