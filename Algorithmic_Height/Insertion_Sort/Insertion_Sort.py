def insertion_sort(arr):
    swap_counts=0
    for i in range(1,len(arr)):
        k=i
        while k>0 and arr[k]<arr[k-1]:
            arr[k],arr[k-1]=arr[k-1],arr[k]
            k-=1
            swap_counts+=1
    return (arr,swap_counts)
arr=[6, 10, 4, 5, 1, 2]

with open("rosalind_ins.txt") as f:
    n=int(f.readline())
    arr=[int(x) for x in f.readline().split(" ")]
print(insertion_sort(arr)[1])
