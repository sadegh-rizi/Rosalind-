with open("rosalind_ms.txt") as f:
    n=int(f.readline())
    arr=[int(x) for x in f.readline().split(" ")]
from merge_two_sorted_arrays import merge_sorted_arrays

def merge_sort(arr):
    if len(arr)==1:
        return arr
    else:
        first_half=merge_sort(arr[:len(arr)//2])
        second_half=merge_sort(arr[len(arr)//2:])
        return merge_sorted_arrays(first_half,second_half)
with open("output.txt","w") as f:
    f.write(" ".join([str(x) for x in merge_sort(arr)]))
    print(" ".join([str(x) for x in merge_sort(arr)]))
print(merge_sort(arr))